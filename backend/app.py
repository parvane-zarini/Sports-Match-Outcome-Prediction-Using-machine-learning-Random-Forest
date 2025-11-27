import os
import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)

# مسیر پوشه دیتاست‌ها
DATASET_DIR = r"C:\Users\Me\OneDrive\Desktop\match_prediction_project\backend\datasets"

# API برای لیست کردن ورزش‌ها (بر اساس فایل‌های موجود)
@app.route('/sports', methods=['GET'])
def get_sports():
    try:
        files = os.listdir(DATASET_DIR)
        datasets = [f.split('.')[0] for f in files if f.endswith('.csv')]
        if not datasets:
            return jsonify({'status': 'error', 'message': 'هیچ دیتاستی یافت نشد.'}), 404
        return jsonify({'status': 'success', 'sports': datasets})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


# API برای پیش‌بینی
@app.route('/predict', methods=['POST'])
def predict_winner():
    try:
        data = request.json
        sport = data.get('sport')
        score1 = int(data.get('score1', 0))
        score2 = int(data.get('score2', 0))

        if not sport or sport.strip() == "":
            return jsonify({'status': 'error', 'message': 'نام ورزش ارسال نشده است.'}), 400

        dataset_path = os.path.join(DATASET_DIR, f"{sport}.csv")
        if not os.path.exists(dataset_path):
            return jsonify({'status': 'error', 'message': 'دیتاست موردنظر یافت نشد.'}), 404

        # خواندن دیتاست
        df = pd.read_csv(dataset_path)

        # برای این مثال فقط پیش‌بینی ساده انجام می‌شود
        winner = "Team 1" if score1 > score2 else "Team 2"
        return jsonify({'status': 'success', 'winner': winner})

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
