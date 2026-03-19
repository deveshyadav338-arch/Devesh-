import joblib
from util import clean

def load_model():
    model = joblib.load('spam_model.pkl')
    vectorizer = joblib.load('vectorizer.pkl')
    return model, vectorizer

def predict_message(message):
    model, vectorizer = load_model()
    cleaned = clean(message)
    message_vec = vectorizer.transform([cleaned])
    prediction = model.predict(message_vec)
    return "Spam" if prediction[0] == 1 else "Ham"
