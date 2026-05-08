import logging
import math
import os


# basic logging setup

logging.basicConfig(level=logging.DEBUG)

logging.debug("This is a debug message")
# Output: DEBUG:root:This is a debug message   

logging.info("This is an info message")
# Output: INFO:root:This is an info message    

logging.warning("This is a warning message")
# Output: WARNING:root:This is a warning message

logging.error("This is an error message")
# Output: ERROR:root:This is an error message

logging.critical("This is a critical message")
# Output: CRITICAL:root:This is a critical message


# Create logger
mylog = logging.getLogger("MyMLProject")
mylog.setLevel(logging.DEBUG)

# Avoid duplicate handlers
if not mylog.handlers:

    # Log message format
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )
    # Save logs to file
    file_handler = logging.FileHandler("ml_project.log", mode="a")
    file_handler.setFormatter(formatter)

    # Show logs in terminal
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Add handlers to logger
    mylog.addHandler(file_handler)
    mylog.addHandler(console_handler)

# Logging messages
mylog.debug("Logger is set up and ready")
mylog.info("Starting ML pipeline")
mylog.warning("Dataset has some missing values")
mylog.error("Failed to load model")
mylog.critical("GPU not found")


# ----- w mode vs a mode -----

# mode="w" clears the log file every time - good for development
# mode="a" keeps all history - good for production and ML training runs


# logging.exception shows full traceback
# Create logger
mylog = logging.getLogger("MyMLProject")
mylog.setLevel(logging.DEBUG)

# Prevent duplicate handlers
if not mylog.handlers:

    # Log format
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    # Save logs in file
    file_handler = logging.FileHandler("ml_project.log", mode="a")
    file_handler.setFormatter(formatter)

    # Show logs in terminal
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Add handlers
    mylog.addHandler(file_handler)
    mylog.addHandler(console_handler)

# Function
def divide(a, b):
    try:
        return a / b

    # Handle division by zero
    except ZeroDivisionError:
        mylog.exception("Tried to divide by zero")
        return None

print(divide(10, 2))

divide(10, 0)


# exc_info=True does the same as exception() but lets you choose the level
def safe_sqrt(x):
    try:
        if x < 0:
            raise ValueError("Cannot take square root of negative number")
        return math.sqrt(x)
    except ValueError:
        mylog.error("ValueError in safe_sqrt", exc_info=True)
        return None

print(safe_sqrt(9))
# Output: 3.0

safe_sqrt(-4)
# Output: 2024-01-15 10:23:45,132 - ERROR - ValueError in safe_sqrt
# Output: Traceback (most recent call last):
# Output:   File "12_logging.py", line X, in safe_sqrt
# Output:     raise ValueError("Cannot take square root of negative number")
# Output: ValueError: Cannot take square root of negative number


# ----- identifying different exception types -----

def process_data(data, index, key):
    try:
        value = data[index][key]
        result = 100 / value
        return result

    except IndexError:
        mylog.exception("IndexError - index out of range, check dataset size")
        return None

    except KeyError:
        mylog.exception("KeyError - column not found, check feature names")
        return None

    except ZeroDivisionError:
        mylog.exception("ZeroDivisionError - a data value was zero")
        return None

    except TypeError:
        mylog.exception("TypeError - wrong data type encountered")
        return None

    except Exception as e:
        mylog.exception("Unexpected error type: " + type(e).__name__)
        return None


sample_data = [{"score": 10}, {"score": 0}, {"score": 5}]

print(process_data(sample_data, 0, "score"))
# Output: 10.0

process_data(sample_data, 10, "score")
# Output: ERROR - IndexError - index out of range, check dataset size
# Output: Traceback ... IndexError: list index out of range

process_data(sample_data, 0, "grade")
# Output: ERROR - KeyError - column not found, check feature names
# Output: Traceback ... KeyError: 'grade'

process_data(sample_data, 1, "score")
# Output: ERROR - ZeroDivisionError - a data value was zero
# Output: Traceback ... ZeroDivisionError: division by zero


# ----- real ml pipeline with proper logging -----

def load_data(filepath):
    mylog.info("Attempting to load data from: " + filepath)
    try:
        # first check if file actually exists on disk
        if not os.path.exists(filepath):
            raise FileNotFoundError("No file found at path: " + filepath)

        if not filepath.endswith(".csv"):
            raise ValueError("Only CSV files are supported")

        # normally this would be: df = pd.read_csv(filepath)
        mylog.info("Data loaded successfully")
        return {"rows": 1000, "features": 10}

    except FileNotFoundError:
        mylog.exception("FileNotFoundError - dataset missing at: " + filepath)
        return None

    except ValueError:
        mylog.exception("ValueError - wrong file format provided")
        return None

    except Exception:
        mylog.exception("Unexpected error while loading data")
        return None


def preprocess(data):
    mylog.info("Starting preprocessing")
    try:
        if data is None:
            raise ValueError("Cannot preprocess None data - data loading likely failed")

        if data["rows"] == 0:
            mylog.warning("Dataset is empty after loading")
            return None

        mylog.debug("Rows: " + str(data["rows"]) + " | Features: " + str(data["features"]))
        mylog.info("Preprocessing complete")
        return data

    except ValueError:
        mylog.exception("ValueError in preprocessing")
        return None

    except Exception:
        mylog.exception("Unexpected error during preprocessing")
        return None


def train(data, epochs):
    if data is None:
        mylog.critical("Training aborted - no data available to train on")
        return False

    mylog.info("Training started for " + str(epochs) + " epochs")

    for epoch in range(1, epochs + 1):
        try:
            loss = 1.0 / epoch   # fake loss going down each epoch
            mylog.debug("Epoch " + str(epoch) + " | Loss: " + str(round(loss, 4)))

            if epoch == epochs:
                mylog.info("Training complete - all epochs finished")

        except Exception:
            mylog.exception("Unexpected error during epoch " + str(epoch))
            return False

    return True


def save_model(trained, path):
    mylog.info("Attempting to save model to: " + path)
    try:
        if not trained:
            raise ValueError("Cannot save - model was not trained successfully")

        # normally: joblib.dump(model, path)
        mylog.info("Model saved successfully to: " + path)
        return True

    except ValueError:
        mylog.exception("ValueError during model save")
        return False

    except PermissionError:
        mylog.exception("PermissionError - cannot write to path: " + path)
        return False

    except Exception:
        mylog.exception("Unexpected error during model save")
        return False


def run_pipeline():
    mylog.info("Pipeline starting")

    # step 1 - load data
    data = load_data("train.csv")   # this file doesnt exist so FileNotFoundError will trigger

    # step 2 - preprocess (will get None since load failed)
    data = preprocess(data)

    # step 3 - train (will abort since data is None)
    success = train(data, 3)

    # step 4 - save model
    saved = save_model(success, "models/model.pkl")

    if success and saved:
        mylog.info("Pipeline finished successfully")
    else:
        mylog.error("Pipeline failed - check logs above for details")


run_pipeline()
# Output: 2024-01-15 10:23:45 - INFO - Pipeline starting
# Output: 2024-01-15 10:23:45 - INFO - Attempting to load data from: train.csv
# Output: 2024-01-15 10:23:45 - ERROR - FileNotFoundError - dataset missing at: train.csv
# Output: Traceback (most recent call last): ...
# Output: FileNotFoundError: No file found at path: train.csv
# Output: 2024-01-15 10:23:45 - INFO - Starting preprocessing
# Output: 2024-01-15 10:23:45 - ERROR - ValueError in preprocessing
# Output: Traceback (most recent call last): ...
# Output: ValueError: Cannot preprocess None data - data loading likely failed
# Output: 2024-01-15 10:23:45 - CRITICAL - Training aborted - no data available to train on
# Output: 2024-01-15 10:23:45 - ERROR - ValueError during model save
# Output: Traceback (most recent call last): ...
# Output: ValueError: Cannot save - model was not trained successfully
# Output: 2024-01-15 10:23:45 - ERROR - Pipeline failed - check logs above for details


# now run with actual data to see the success path
def run_pipeline_success():
    mylog.info("Pipeline starting with real data")

    # manually passing data as if file loaded correctly
    data = {"rows": 1000, "features": 10}
    data = preprocess(data)
    success = train(data, 3)
    saved = save_model(success, "models/model.pkl")

    if success and saved:
        mylog.info("Pipeline finished successfully")
    else:
        mylog.error("Pipeline failed")


run_pipeline_success()
# Output: 2024-01-15 10:23:45 - INFO - Pipeline starting with real data
# Output: 2024-01-15 10:23:45 - INFO - Starting preprocessing
# Output: 2024-01-15 10:23:45 - DEBUG - Rows: 1000 | Features: 10
# Output: 2024-01-15 10:23:45 - INFO - Preprocessing complete
# Output: 2024-01-15 10:23:45 - INFO - Training started for 3 epochs
# Output: 2024-01-15 10:23:45 - DEBUG - Epoch 1 | Loss: 1.0
# Output: 2024-01-15 10:23:45 - DEBUG - Epoch 2 | Loss: 0.5
# Output: 2024-01-15 10:23:45 - DEBUG - Epoch 3 | Loss: 0.3333
# Output: 2024-01-15 10:23:45 - INFO - Training complete - all epochs finished
# Output: 2024-01-15 10:23:45 - INFO - Model saved successfully to: models/model.pkl
# Output: 2024-01-15 10:23:45 - INFO - Pipeline finished successfully


# ----- checking the log file -----

if os.path.exists("ml_project.log"):
    mylog.info("Reading log file summary")
    with open("ml_project.log", "r") as f:
        lines = f.readlines()

    print("Total log entries:", len(lines))
    print("Last 5 entries:")
    for line in lines[-5:]:
        print(line.strip())