import pickle
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, "tfidf_vectorizer.pkl"), "rb") as f:
    tfidf = pickle.load(f)

with open(os.path.join(BASE_DIR, "sentiment_model.pkl"), "rb") as f:
    model = pickle.load(f)

label_map = {
    0: "sadness",
    1: "anger",
    2: "love",
    3: "surprise",
    4: "fear",
    5: "joy"
}

def predict_sentiment(text):
    text_tfidf = tfidf.transform([text])
    pred = model.predict(text_tfidf)[0]
    return label_map[pred]
