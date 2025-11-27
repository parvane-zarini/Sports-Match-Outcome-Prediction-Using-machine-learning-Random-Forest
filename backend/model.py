import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import os
from data_loader import load_data

MODEL_DIR = "backend/models"

def train_and_save_model(sport):
    """آموزش مدل برای ورزش انتخاب‌شده و ذخیره آن"""
    df = load_data(sport)
    
    X = df[['Score 1', 'Score 2']]
    y = df['Winner']

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)

    if not os.path.exists(MODEL_DIR):
        os.makedirs(MODEL_DIR)

    model_path = os.path.join(MODEL_DIR, f"model_{sport}.pkl")
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)

def load_model(sport):
    """بارگذاری مدل آموزش‌دیده"""
    model_path = os.path.join(MODEL_DIR, f"model_{sport}.pkl")
    if not os.path.exists(model_path):
        train_and_save_model(sport)

    with open(model_path, 'rb') as f:
        return pickle.load(f)

def predict_match_winner(sport, score1, score2):
    """پیش‌بینی برنده مسابقه"""
    model = load_model(sport)
    prediction = model.predict([[score1, score2]])
    return prediction[0]
