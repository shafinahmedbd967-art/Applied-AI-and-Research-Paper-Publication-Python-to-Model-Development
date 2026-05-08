# basic try except - simplest form
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
# Output: Cannot divide by zero


# without try except this would crash the whole program
# result = 10 / 0
# ZeroDivisionError: division by zero


# catching the exception object to see the message
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Error caught:", e)
# Output: Error caught: division by zero


# multiple except blocks

def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Division by zero is not allowed")
    except TypeError:
        print("Both values must be numbers")

print(safe_divide(10, 2))
# Output: 5.0

safe_divide(10, 0)
# Output: Division by zero is not allowed

safe_divide(10, "five")
# Output: Both values must be numbers


# catching multiple errors in one line
def parse_input(value):
    try:
        return int(value)
    except (ValueError, TypeError) as e:
        print("Could not parse input:", e)
        return None

print(parse_input("42"))
# Output: 42

print(parse_input("hello"))
# Output: Could not parse input: invalid literal for int() with base 10: 'hello'
# Output: None

print(parse_input(None))
# Output: Could not parse input: int() argument must be a string, a bytes-like object or a real number, not 'NoneType'
# Output: None


# finally block

# finally always runs no matter what
def read_data(filename):
    print("Opening file...")
    try:
        f = open(filename, "r")
        data = f.read()
        print("File read successfully")
        return data
    except FileNotFoundError:
        print("File not found:", filename)
        return None
    finally:
        print("This always runs - cleanup happens here")

read_data("data.csv")
# Output: Opening file...
# Output: File not found: data.csv
# Output: This always runs - cleanup happens here

# even when successful, finally still runs
# read_data("real_file.csv")
# Output: Opening file...
# Output: File read successfully
# Output: This always runs - cleanup happens here


# ----- else block with try except -----

# else runs only when NO exception happened
def load_number(s):
    try:
        num = int(s)
    except ValueError:
        print("Not a valid number")
    else:
        print("Successfully loaded:", num)  # only runs if no error
    finally:
        print("Attempt finished")

load_number("100")
# Output: Successfully loaded: 100
# Output: Attempt finished

load_number("abc")
# Output: Not a valid number
# Output: Attempt finished


# ----- raising exceptions manually -----

# sometimes we want to raise our own exception
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return age

try:
    set_age(-5)
except ValueError as e:
    print("Invalid age:", e)
# Output: Invalid age: Age cannot be negative

try:
    set_age(200)
except ValueError as e:
    print("Invalid age:", e)
# Output: Invalid age: Age seems unrealistic


# ----- custom exceptions -----

# we can make our own exception classes
class ModelNotTrainedError(Exception):
    pass

class InvalidInputShapeError(Exception):
    def __init__(self, expected, got):
        self.expected = expected
        self.got = got
        super().__init__("Expected shape " + str(expected) + " but got " + str(got))


# using custom exception
def predict(model_trained, input_data):
    if not model_trained:
        raise ModelNotTrainedError("Model must be trained before prediction")
    if len(input_data) != 3:
        raise InvalidInputShapeError(3, len(input_data))
    return sum(input_data) * 0.5   # fake prediction

try:
    predict(False, [1, 2, 3])
except ModelNotTrainedError as e:
    print("Model error:", e)
# Output: Model error: Model must be trained before prediction

try:
    predict(True, [1, 2])
except InvalidInputShapeError as e:
    print("Shape error:", e)
# Output: Shape error: Expected shape 3 but got 2

try:
    result = predict(True, [1, 2, 3])
    print("Prediction:", result)
except (ModelNotTrainedError, InvalidInputShapeError) as e:
    print("Failed:", e)
# Output: Prediction: 3.0


# ----- catching all exceptions -----

# use this carefully - catching everything can hide real bugs
def risky_operation(data):
    try:
        result = data["value"] / data["divisor"]
        return result
    except KeyError as e:
        print("Missing key in data:", e)
    except ZeroDivisionError:
        print("Divisor cannot be zero")
    except Exception as e:
        # catches anything else we didnt expect
        print("Unexpected error:", type(e).__name__, "-", e)

risky_operation({"value": 10, "divisor": 2})
# Output: 5.0  (no error)

risky_operation({"value": 10})
# Output: Missing key in data: 'divisor'

risky_operation({"value": 10, "divisor": 0})
# Output: Divisor cannot be zero

risky_operation("not a dict")
# Output: Unexpected error: TypeError - string indices must be integers


# ----- machine learning real world use cases -----

import os

# 1. data loading with error handling
def load_dataset(filepath):
    try:
        if not os.path.exists(filepath):
            raise FileNotFoundError("Dataset not found at: " + filepath)

        # simulating reading a csv
        print("Loading dataset from:", filepath)
        # normally: df = pd.read_csv(filepath)
        return {"rows": 1000, "cols": 10}   # fake return for demo

    except FileNotFoundError as e:
        print("Data loading failed:", e)
        return None
    except Exception as e:
        print("Unexpected error while loading data:", e)
        return None

result = load_dataset("train.csv")
# Output: Data loading failed: Dataset not found at: train.csv

print(result)
# Output: None


# 2. preprocessing - handling bad values
def safe_normalize(value, min_val, max_val):
    try:
        if min_val == max_val:
            raise ZeroDivisionError("min and max are the same, cant normalize")
        normalized = (value - min_val) / (max_val - min_val)
        return normalized
    except TypeError:
        print("Value must be a number, got:", type(value).__name__)
        return None
    except ZeroDivisionError as e:
        print("Normalization error:", e)
        return None

print(safe_normalize(50, 0, 100))
# Output: 0.5

print(safe_normalize("hello", 0, 100))
# Output: Value must be a number, got: str
# Output: None

print(safe_normalize(50, 100, 100))
# Output: Normalization error: min and max are the same, cant normalize
# Output: None


# 3. model training loop with error handling
def train_model(epochs, data):
    trained = False
    for epoch in range(epochs):
        try:
            if not data:
                raise ValueError("Training data is empty")

            # simulating a training step
            loss = 1.0 / (epoch + 1)    # fake loss going down

            if loss != loss:             # checking for NaN (NaN != NaN is always True)
                raise ValueError("Loss became NaN - training is unstable")

            print("Epoch", epoch + 1, "| Loss:", round(loss, 4))
            trained = True

        except ValueError as e:
            print("Training error at epoch", epoch + 1, ":", e)
            break
        except MemoryError:
            print("Out of memory at epoch", epoch + 1)
            break
        finally:
            pass   # could save checkpoint here every epoch

    return trained

status = train_model(3, [1, 2, 3])
# Output: Epoch 1 | Loss: 1.0
# Output: Epoch 2 | Loss: 0.5
# Output: Epoch 3 | Loss: 0.3333

print("Training successful:", status)
# Output: Training successful: True

status2 = train_model(3, [])
# Output: Training error at epoch 1 : Training data is empty

print("Training successful:", status2)
# Output: Training successful: False


# 4. model saving and loading
def save_model(model, path):
    try:
        # normally: joblib.dump(model, path) or model.save(path)
        if model is None:
            raise ValueError("Cannot save a None model")
        print("Model saved to:", path)
        return True
    except ValueError as e:
        print("Save failed:", e)
        return False
    except PermissionError:
        print("No permission to write to:", path)
        return False
    except Exception as e:
        print("Unexpected save error:", e)
        return False

save_model(None, "model.pkl")
# Output: Save failed: Cannot save a None model

save_model("fake_model_object", "model.pkl")
# Output: Model saved to: model.pkl


# 5. prediction with input validation
def predict_price(features):
    expected_features = 5

    try:
        if not isinstance(features, list):
            raise TypeError("Features must be a list")

        if len(features) != expected_features:
            raise InvalidInputShapeError(expected_features, len(features))

        if any(f is None for f in features):
            raise ValueError("Features contain None values - fill missing data first")

        # fake prediction
        prediction = sum(features) * 1.5
        return prediction

    except TypeError as e:
        print("Type error:", e)
    except InvalidInputShapeError as e:
        print("Shape error:", e)
    except ValueError as e:
        print("Value error:", e)

print(predict_price([1.2, 3.4, 2.1, 0.8, 1.5]))
# Output: 13.5

predict_price("not a list")
# Output: Type error: Features must be a list

predict_price([1.2, 3.4])
# Output: Shape error: Expected shape 5 but got 2

predict_price([1.2, None, 2.1, 0.8, 1.5])
# Output: Value error: Features contain None values - fill missing data first