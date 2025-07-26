# 💫 Friendship Compatibility Predictor

A machine learning-based web application that predicts whether two individuals are likely to be **good friends** based on their personal traits, preferences, and hobbies. The project uses Python for data handling and model training and Streamlit to build an intuitive, interactive frontend.

---

## 🧠 Overview

The goal of this project is to simulate how compatible two people are as friends using machine learning techniques. It considers attributes like name, gender, age, hobbies, favorite color, food preference, and more. This is a fun and educational project to explore classification models and deploy them using Streamlit.

---

## 🚀 Features

- ✅ Input form for two people's details
- ✅ Uses a pre-trained ML model to predict friendship compatibility
- ✅ Streamlit interface with real-time prediction
- ✅ Simple, engaging UI
- ✅ Supports Logistic Regression, Decision Tree, and Random Forest models

---

## 📂 Folder Structure

Friendship-Compatibility-Predictor/
│
├── app.py # Streamlit web application
├── train_model.py # Model training script
├── model.pkl # Saved trained model
├── friend_data.csv # Dataset of past friendships
├── requirements.txt # Dependencies
└── README.md # Project documentation

---

## 🔍 How it Works

1. **Data Preparation**  
   The dataset `friend_data.csv` includes past examples of friendships and the related attributes.

2. **Model Training**  
   Run `train_model.py` to preprocess data and train using Logistic Regression, Decision Tree, or Random Forest.

3. **Prediction**  
   The `app.py` Streamlit application loads the model and predicts compatibility when two users enter their details.

---

## 🛠️ Tech Stack

- **Programming Language:** Python  
- **Libraries:** 
  - `pandas`, `numpy` – Data manipulation  
  - `scikit-learn` – Machine learning  
  - `joblib` – Model serialization  
  - `streamlit` – Web app interface  

---


