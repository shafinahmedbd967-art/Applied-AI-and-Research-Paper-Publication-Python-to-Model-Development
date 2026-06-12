from flask import Flask, render_template, request, jsonify
from transformers import pipeline

sentiment_classifier = pipeline(
    'sentiment-analysis', 
    model='distilbert-base-uncased-finetuned-sst-2-english')


app = Flask(__name__)

# "/" route to display welcome
@app.route('/')
def welcome():
    return "Welcome to the Flask App!"

@app.route('/hello/<name>')
def hello(name):
    return f"<h1>Hello, {len(name)}!</h1>"

# render html
@app.route('/greet')
def greet():
    return """
    <html>
        <head>
            <title>Welcome to the Flask App</title>    
        </head>
        <body>
            <h1>Greetings!</h1>
            <p>Welcome to the Flask App.</p>
        </body>
    </html>
    """

# render html from template
@app.route('/welcome')
def welcome_template():
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        sentence = request.form['sentence']
        result = sentiment_classifier(sentence)[0]
        # upto 2 decimal places
        confidence = round(result['score']*100, 2)
        label = result['label']
        return render_template('form.html', sentence=sentence, confidence=confidence, label=label)
    return render_template('form.html')

# @app.route('/analyze', methods=['POST'])
# def analyze():
#     sentence = request.form['sentence']
#     result = sentiment_classifier(sentence)[0]
#     # upto 2 decimal places
#     confidence = round(result['score']*100, 2)
#     label = result['label']
#     # Perform sentiment analysis on the sentence
#     # For now, we'll just return the sentence
#     return render_template('form.html', sentence=sentence, confidence=confidence, label=label)

# make api
@app.route('/api/sentiment', methods=['POST'])
def api_sentiment():
    data = request.get_json()
    sentence = data['sentence']
    result = sentiment_classifier(sentence)[0]
    confidence = round(result['score']*100, 2)
    label = result['label']
    return jsonify({
        'sentence': sentence,
        'confidence': confidence,
        'label': label
    })

if __name__ == '__main__': 
    app.run(debug=True)