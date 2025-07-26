import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# 📌 TITLE & INTRO
# -----------------------------
st.title("🤝 Friendship Compatibility Predictor")
st.write("""
Fill in the details for **Person A** and **Person B**.
Pick their hobbies — the app will check how many they share!
Select a model to use for prediction.
""")

# -----------------------------
# 📌 MODEL SELECTOR
# -----------------------------
model_choice = st.selectbox(
    "Select the model you want to use:",
    ["Logistic Regression", "Decision Tree", "Random Forest"]
)

# Load the chosen model
if model_choice == "Logistic Regression":
    model = joblib.load("logtree_model.pkl")
elif model_choice == "Decision Tree":
    model = joblib.load("decision_model.pkl")
else:
    model = joblib.load("forest_model.pkl")

# -----------------------------
# 📌 INPUTS — PERSON A
# -----------------------------
st.header("Person A Details")
age_a = st.number_input("Age of Person A", 18, 100, 25)
income_a = st.number_input("Monthly Income of Person A (₹)", 0, 1000000, 30000)
spending_a = st.selectbox("Spending habit of Person A", ["Saver", "Average", "Spender"])
personality_a = st.selectbox("Personality type of Person A", ["Introvert", "Extrovert"])
planner_a = st.selectbox("Is Person A a planner?", ["Yes", "No"])

# -----------------------------
# 📌 INPUTS — PERSON B
# -----------------------------
st.header("Person B Details")
age_b = st.number_input("Age of Person B", 18, 100, 24)
income_b = st.number_input("Monthly Income of Person B (₹)", 0, 1000000, 28000)
spending_b = st.selectbox("Spending habit of Person B", ["Saver", "Average", "Spender"])
personality_b = st.selectbox("Personality type of Person B", ["Introvert", "Extrovert"])
planner_b = st.selectbox("Is Person B a planner?", ["Yes", "No"])

# -----------------------------
# 📌 SHARED INTERESTS — HOBBIES & MUSIC
# -----------------------------
st.header("Shared Interests")

hobby_options = [
    "Reading",
    "Sports",
    "Gaming",
    "Cooking",
    "Travel",
    "Music",
    "Movies",
    "Art",
    "Dancing",
    "Fitness"
]

hobbies_a = st.multiselect("Person A's hobbies:", hobby_options, default=["Reading", "Music"])
hobbies_b = st.multiselect("Person B's hobbies:", hobby_options, default=["Music", "Travel"])

# Calculate overlap
shared_hobbies = len(set(hobbies_a).intersection(set(hobbies_b)))

# Music overlap slider
music = st.slider("Shared music interest level (0 = no match, 2 = perfect match)", 0, 2, 1)

# -----------------------------
# 📌 FEATURE ENGINEERING
# -----------------------------
age_gap = abs(age_a - age_b)
income_gap = abs(income_a - income_b)
same_spending = int(spending_a == spending_b)
same_personality = int(personality_a == personality_b)
same_planner = int(planner_a == planner_b)

X_new = [[
    age_gap,
    income_gap,
    same_spending,
    same_personality,
    same_planner,
    shared_hobbies,
    music
]]

# -----------------------------
# 📌 PREDICT
# -----------------------------
if st.button("Check Friendship Compatibility"):
    prediction = model.predict(X_new)[0]
    probability = model.predict_proba(X_new)[0][1]

    if prediction == 1:
        st.success(f"✅ They are likely to be good friends! (Probability: {probability:.2%})")
    else:
        st.error(f"❌ They may not be good friends. (Probability: {probability:.2%})")

    st.info(f"Used model: **{model_choice}**")

