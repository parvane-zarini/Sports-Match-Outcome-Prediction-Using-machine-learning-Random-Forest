import pandas as pd
import os

DATASET_DIR = "backend/datasets"

def load_data(sport):
    """بارگذاری دیتاست مربوط به ورزش انتخاب‌شده"""
    file_path = os.path.join(DATASET_DIR, f"match_score_dataset_{sport}.csv")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"دیتاست {sport} یافت نشد!")
    
    df = pd.read_csv(file_path)
    if 'Score 1' not in df.columns or 'Score 2' not in df.columns or 'Winner' not in df.columns:
        raise ValueError(f"فرمت دیتاست {sport} نامعتبر است!")
    
    return df[['Score 1', 'Score 2', 'Winner']]
