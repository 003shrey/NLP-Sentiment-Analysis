# NLP Sentiment Analysis

A sentiment analysis application that predicts emotions from text using machine learning. The model classifies text into six emotion categories: sadness, anger, love, surprise, fear, and joy.

## Features

- Emotion classification into 6 categories
- Interactive web interface built with Streamlit
- Pre-trained machine learning model using TF-IDF vectorization
- Simple prediction API

## Dataset

The model is trained on a dataset containing 16,000 labeled text samples. Each sample is associated with one of six emotions: sadness, anger, love, surprise, fear, or joy.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/003shrey/NLP-Sentiment-Analysis.git
cd NLP-Sentiment-Analysis
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Web Application

Start the Streamlit web interface:
```bash
streamlit run app.py
```

The application will open in your browser where you can enter text and get emotion predictions.

### Using the Prediction Module

You can also use the prediction module directly in your Python code:

```python
from predict import predict_sentiment

text = "I am feeling very happy today"
emotion = predict_sentiment(text)
print(f"Predicted Emotion: {emotion}")
```

## Model Information

- Algorithm: Machine Learning classifier with TF-IDF vectorization
- Input: Raw text
- Output: One of six emotions (sadness, anger, love, surprise, fear, joy)
- Pre-trained models included: `sentiment_model.pkl` and `tfidf_vectorizer.pkl`

## Project Structure

```
.
├── app.py                      # Streamlit web application
├── predict.py                  # Prediction module
├── Sentimental_Analysis.ipynb  # Model training notebook
├── train.txt                   # Training dataset
├── sentiment_model.pkl         # Trained model
├── tfidf_vectorizer.pkl        # TF-IDF vectorizer
└── requirements.txt            # Python dependencies
```

## Requirements

- streamlit
- scikit-learn
- numpy

## License

This project is available under the terms specified in the LICENSE file.
