#  Sports Match Outcome Prediction Using Random Forest

A data-driven machine learning system designed to **predict match outcomes across 12 different sports** using a **Random Forest Classifier**.  
This project combines a Python-based backend with a clean and intuitive web-based frontend to deliver accurate and interactive sports predictions.

---

##  Overview

This project focuses on applying **machine learning** to forecast the outcomes of sports matches using historical data.  
By training a **Random Forest model** on curated datasets from **twelve sports**, the system learns patterns between team performance, match statistics, and win outcomes.

Once trained, users can select a sport, choose two teams, and instantly receive a **prediction of the likely winner**.  
This project demonstrates how data science techniques can be utilized to create intelligent, real-world predictive systems in competitive sports.

---

##  Project Structure

The project consists of two major components:

### 🔹 Backend (Python)
- Loads and merges datasets from 12 sports  
- Cleans and standardizes inconsistent columns  
- Applies **Label Encoding** for team names  
- Trains the **Random Forest Classifier**  
- Generates predictions based on user inputs  

### 🔹 Frontend (HTML, CSS, JavaScript)
- Simple and modern UI  
- Dropdowns for selecting a sport and two teams  
- Displays instant prediction results  

<p align="center">
  <img width="573" height="268" src="https://github.com/user-attachments/assets/f42c8631-9bd5-429b-866a-550faf45127b" />
</p>

---

##  Data Preparation & Modeling

To ensure compatibility across datasets, all twelve CSV files were:

- **Loaded & cleaned**
- **Standardized** (column names unified across sports)
- **Encoded using Label Encoding**

After preprocessing, a **Random Forest Classifier** was trained due to its robustness and strong handling of complex data patterns.

<p align="center">
  <img width="616" height="93" src="https://github.com/user-attachments/assets/2f562903-266c-4054-b7fc-3dfc444fb400" /><br>
  <img width="616" height="122" src="https://github.com/user-attachments/assets/96afc19d-e648-4239-b157-af13a0b6ea8b" /><br>
  <img width="616" height="46" src="https://github.com/user-attachments/assets/5f181f0b-d536-4f7f-8297-2d3f2e00dc88" /><br>
  <img width="616" height="120" src="https://github.com/user-attachments/assets/19369e98-a1d0-4856-a8ef-92cc998dcdb9" />
</p>

---

##  Model Performance

The model achieved an **accuracy of ~70%**, which is strong considering the diverse nature of sports and limited features available.  
This is due to:

- The variety of match data  
- The robustness of the Random Forest model  
- Consistent preprocessing  

---

##  User Interface

A clean UI allows users to:

1. Select a sport  
2. Choose two teams  
3. Instantly get a prediction  

<p align="center">
  <img width="616" height="280" src="https://github.com/user-attachments/assets/03a4f045-0226-431f-b0e9-6ca39aca2aa3" />
</p>

---

##  Challenges & Limitations

- **Unseen team labels:** Teams not present in training data cannot be encoded.  
- **Missing contextual features:** Weather, player conditions, strategies, etc.  
- **Dataset inconsistencies:** Different formats across sports.  

---

##  Future Improvements

Potential enhancements:

- Adding contextual features (venue, recent form, scoring trends)  
- Using advanced ML models like **XGBoost** or **Neural Networks**  
- Real-time prediction updates  
- Player-level statistics  

---

##  Technologies Used

- **Backend:** Python  
- **Frontend:** HTML, CSS, JavaScript  
- **Libraries:** scikit-learn, pandas, numpy  

---

##  Installation & Setup

1. Clone the repository:
```bash
git clone <your-repository-link>
```

2. Install backend dependencies:
```bash
pip install -r requirements.txt
python app.py
```

3. Run frontend:
- Open `index.html` in your browser

---

##  License

MIT License

---

**Developer:** Mehdi Tootkar Bidarigh
