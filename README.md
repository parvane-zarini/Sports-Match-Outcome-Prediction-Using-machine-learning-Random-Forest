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

### **🔹 Backend (Python)**
- Loads and merges datasets from 12 sports  
- Cleans and standardizes inconsistent columns  
- Applies **Label Encoding** for team names  
- Trains the **Random Forest Classifier**  
- Generates predictions based on user inputs  

### **🔹 Frontend (HTML, CSS, JavaScript)**
- Simple and modern UI  
- Dropdowns for selecting a sport and two teams  
- Displays instant prediction results  

---

##  Data Preparation & Modeling

All datasets were unified through cleaning, standardization, and **Label Encoding**.  
A **Random Forest Classifier** was then trained due to its strong performance on multi-feature datasets.

---

##  Model Performance

The model achieved an **accuracy of ~70%**, which is strong considering the diverse nature of sports and limited feature availability.

---

##  User Interface

A clean UI allows users to pick a sport, select two teams, and instantly see the predicted winner.

---

##  Challenges & Limitations

- Unseen team labels not present in training  
- Missing contextual real-world features  
- Dataset inconsistencies across sports  

---

##  Future Improvements

- Adding richer features (recent stats, venue, weather)  
- Testing models such as **XGBoost** or **Neural Networks**  
- Real-time prediction updates  
- Deeper team/player statistics  

---

##  Technologies Used

- **Python** (backend)  
- **HTML, CSS, JavaScript** (frontend)  
- **scikit-learn**, pandas, numpy  

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
