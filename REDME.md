# 🚲 Bike Rental Demand Prediction

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Regression-orange)
![Streamlit](https://img.shields.io/badge/Deployment-Streamlit-red)
![CatBoost](https://img.shields.io/badge/Model-CatBoost-green)
![License](https://img.shields.io/badge/License-MIT-purple)

An End-to-End Machine Learning Regression Project to predict hourly bike rental demand using weather conditions, seasonal patterns, and time-based features.

🚀 **Live Demo:** https://akhlaque03-bike-rental-demand-predictor.streamlit.app/

##  Overview

This project focuses on building a complete Machine Learning pipeline, from data preprocessing and exploratory analysis to model optimization and deployment.

The final model, **Hyperparameter Tuned CatBoost Regressor**, is deployed using Streamlit to provide real-time bike rental demand predictions.
---

#  Project Overview

Bike Rental Demand Prediction is an end-to-end Machine Learning Regression project developed to estimate the number of bikes expected to be rented in a given hour.

The project demonstrates the complete machine learning pipeline, including:

* Data Cleaning
* Exploratory Data Analysis (EDA)
* Feature Engineering
* Model Building
* Model Comparison
* Hyperparameter Tuning
* Streamlit Deployment

The final application enables users to predict bike rental demand interactively by selecting weather, seasonal, and time-related conditions.

---

#  Project Objectives

* Predict hourly bike rental demand accurately.
* Compare multiple regression algorithms.
* Improve model performance using Hyperparameter Tuning.
* Deploy the best-performing model with Streamlit.
* Build an interactive and user-friendly prediction application.

---

# 📂 Dataset Information

The dataset contains historical hourly bike rental records along with weather and calendar-related information.

## Input Features

* Hour
* Month
* Weekday
* Temperature
* Feels Like Temperature
* Humidity
* Wind Speed
* Season
* Year
* Holiday
* Working Day
* Weather Situation
* Rush Hour

## Target Variable

**Bike Rental Count (cnt)**

---

# 🛠 Data Preprocessing

The following preprocessing techniques were applied before model training:

* Missing Value Analysis
* Duplicate Record Removal
* Outlier Detection
* Feature Engineering
* One-Hot Encoding
* Feature Selection

---

# 📊 Exploratory Data Analysis

Exploratory Data Analysis was performed to understand data distribution and feature relationships.

### Analysis Performed

* Univariate Analysis
* Bivariate Analysis
* Correlation Analysis
* Distribution Analysis
* Feature Importance Analysis

---

# 🤖 Machine Learning Models Evaluated

The following regression algorithms were trained and evaluated:

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor
* Gradient Boosting Regressor
* K-Nearest Neighbors (KNN) Regressor
* XGBoost Regressor
* LightGBM Regressor
* CatBoost Regressor
* Support Vector Regressor (SVR)

---

# 📈 Baseline Model Comparison

| Model | R² Score |
| ------------------------- | -------: |
| CatBoost Regressor | 0.9535 |
| XGBoost Regressor | 0.9513 |
| LightGBM Regressor | 0.9484 |
| Random Forest Regressor | 0.9465 |
| Decision Tree Regressor | 0.8935 |
| Gradient Boosting Regressor | 0.8628 |
| KNN Regressor | 0.8053 |
| Linear Regression | 0.5860 |
| Support Vector Regressor (SVR) | 0.5554 |
---

# ⚙ Hyperparameter Tuning

## ⚙ Hyperparameter Tuning

To improve model performance, hyperparameter optimization was performed using **RandomizedSearchCV** with cross-validation.

### Tuned Models

The following regression models were optimized:

- CatBoost Regressor
- XGBoost Regressor
- LightGBM Regressor
- Random Forest Regressor

The tuned models achieved better generalization performance compared to baseline models.

---

## 🏆 Best Performing Model

The final selected model is:

### 🥇 CatBoost Regressor (Hyperparameter Tuned)

CatBoost achieved the best performance among all evaluated regression models after hyperparameter optimization.

### Final Performance

| Metric | Score |
|---|---:|
| MAE | 21.9912 |
| MSE | 1280.1439 |
| RMSE | 35.7791 |
| R² Score | 0.9596 |

---

# 💻 Streamlit Web Application

An interactive Streamlit application was developed to allow users to predict bike rental demand in real time.

### User Inputs

* Hour
* Month
* Weekday
* Temperature
* Feels Like Temperature
* Humidity
* Wind Speed
* Season
* Year
* Holiday
* Working Day
* Weather Situation
* Rush Hour

### Prediction Output

* 🚲 Estimated Bike Rentals per Hour
* 🤖 Model Used: CatBoost Regressor

---

# 📷 Application Screenshots

## 🏠 Home Page

![Home Page](images/home_page.png)

---

## 🚲 Prediction Result

![Prediction Result](images/prediction_result.png)

---

## 📊 Model Comparison

![Model Comparison](images/model_comparison.png)

---

# 📁 Project Structure

```text
Bike-Rental-Demand-Prediction/
│
├── app.py
├── Bike_Rental_Demand_Prediction.ipynb
├── dataset.csv
├── catboost_final_model.pkl
├── feature_columns.pkl
├── requirements.txt
├── README.md
├── .gitignore
└── images/
    ├── home_page.png
    ├── prediction_result.png
    └── model_comparison.png
```

---

##  Technologies Used

### Programming & Data Processing
- Python
- Pandas
- NumPy

### Data Visualization
- Matplotlib
- Seaborn

### Machine Learning
- Scikit-learn
- CatBoost
- XGBoost
- LightGBM

### Deployment & Tools
- Streamlit
- Joblib
- Jupyter Notebook
- GitHub
---

# 🚀 Installation

```bash
git clone <repository-url>

cd Bike-Rental-Demand-Prediction

pip install -r requirements.txt

streamlit run app.py
```

---

## 🔮 Future Enhancements

Potential improvements for this project:

- 🌦️ Real-Time Weather API Integration
- 📊 Advanced Interactive Dashboard
- ⚙️ Automated Model Retraining Pipeline
- 📈 Model Monitoring and Performance Tracking
- 🚀 CI/CD Pipeline Integration

---

## 👨‍💻 Author

**Akhlaque Alam**

Data Science Enthusiast with hands-on experience in:

- Python
- SQL
- Machine Learning
- Data Analysis
- Streamlit Deployment

Passionate about building machine learning solutions and developing data-driven applications.

Open to Data Science and Machine Learning opportunities.

---

⭐ **If you found this project useful, consider giving it a Star.**
