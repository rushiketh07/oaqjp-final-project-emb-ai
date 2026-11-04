# Emotion Detector AI Web Application

An AI-driven Emotion Detection web application developed using Python, IBM Watson NLP runtime service, Flask web framework, Unittest, and Pylint. The application processes user text, analyzes underlying emotional sentiments (anger, disgust, fear, joy, and sadness), and identifies the dominant emotion.

---

## 🏛 Architecture Summary

The Emotion Detector application follows a clean modular client-server architecture:

```
+-------------------------------------------------------+
|                    Client Browser                     |
|           (HTML5, Bootstrap 4, AJAX / Vanilla JS)     |
+---------------------------+---------------------------+
                            | HTTP GET /emotionDetector
                            v
+-------------------------------------------------------+
|                 Flask Web Server (server.py)          |
|      - Port: 5000, Host: 0.0.0.0                      |
|      - Handles routing, request parsing, & formatting |
+---------------------------+---------------------------+
                            | Function Call
                            v
+-------------------------------------------------------+
|          EmotionDetection Package (Python Module)     |
|      - EmotionDetection/__init__.py                   |
|      - EmotionDetection/emotion_detection.py          |
|      - Error handling for status code 400             |
+---------------------------+---------------------------+
                            | REST API (POST)
                            v
+-------------------------------------------------------+
|              IBM Watson NLP Runtime Service           |
|      - Endpoint: NlpService/EmotionPredict            |
|      - Model: emotion_aggregated-workflow_lang_en     |
+-------------------------------------------------------+
```

1. **Frontend Interface (`templates/index.html` & `static/mywebscript.js`)**:
   - Modern, responsive web user interface built with Bootstrap 4.
   - Asynchronous JavaScript (AJAX / XMLHttpRequest) passes text input to the backend without page reload.

2. **Backend Application (`server.py`)**:
   - Lightweight, production-grade Flask server exposing `/` and `/emotionDetector` endpoints.
   - Parses query parameters, delegates emotion extraction to the custom package, and formats human-readable response strings.
   - Evaluated to a perfect **10.00/10** code quality score using Pylint static code analysis.

3. **Emotion Detection Core Package (`EmotionDetection/`)**:
   - Self-contained, importable Python package encapsulating REST API communications with Watson NLP.
   - Computes emotion scores for `anger`, `disgust`, `fear`, `joy`, and `sadness`, determining the `dominant_emotion`.
   - Incorporates robust error handling for blank/invalid inputs (HTTP 400).

4. **Testing Suite (`test_emotion_detection.py`)**:
   - Automated unit test suite utilizing Python's built-in `unittest` library to validate accuracy across core emotion classifications.

---

## 📂 Repository Directory Structure

```text
oaqjp-final-project-emb-ai/
├── EmotionDetection/
│   ├── __init__.py               # Package initialization exposing emotion_detector
│   └── emotion_detection.py      # Watson NLP API integration & score extraction
├── static/
│   └── mywebscript.js            # Asynchronous AJAX client script
├── templates/
│   └── index.html                # Responsive web application interface
├── .gitignore                    # Git ignore configuration
├── README.md                     # Project documentation & architecture overview
├── requirements.txt              # Project package dependencies
├── server.py                     # Flask application deployment script (Pylint 10/10)
└── test_emotion_detection.py     # Unittest test cases for emotion prediction
```

---

## 🚀 Setup & Installation Instructions

### 1. Prerequisites
- Python 3.8 to 3.13 installed
- Git installed and configured
- Pip package manager

### 2. Clone the Repository
```bash
git clone https://github.com/rushiketh07/oaqjp-final-project-emb-ai.git
cd oaqjp-final-project-emb-ai
```

### 3. Create and Activate a Virtual Environment
```bash
# Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the Automated Unit Tests
Verify model predictions and test suite integrity:
```bash
python3 test_emotion_detection.py
```
*Expected Output:*
```text
.....
----------------------------------------------------------------------
Ran 5 tests in 0.85s

OK
```

### 6. Perform Static Code Analysis (Pylint)
Ensure high code quality and docstring compliance:
```bash
pylint server.py
```
*Expected Output:*
```text
--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
```

### 7. Run the Flask Web Server
```bash
python3 server.py
```
The application will launch on `http://localhost:5000` (or `http://0.0.0.0:5000`).

---

## 🔌 API Specification

### Endpoint: `/emotionDetector`
- **Method:** `GET`
- **Query Parameter:** `textToAnalyze` (string)

#### Successful Response (HTTP 200 OK):
```text
For the given statement, the system response is 'anger': 0.0051, 'disgust': 0.0016, 'fear': 0.0058, 'joy': 0.9821 and 'sadness': 0.0152. The dominant emotion is joy.
```

#### Blank / Invalid Input Response (HTTP 200 OK):
```text
Invalid text! Please try again!
```

---

## 📄 License
This project is licensed under the Apache 2.0 License.

