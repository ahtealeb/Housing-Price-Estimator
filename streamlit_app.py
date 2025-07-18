import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load trained model
model = joblib.load("house_price_model.pkl")

# Define feature names
feature_columns = ["Area", "Bedroom", "Bathroom", "Floor", "View", "Facing", "Elevator", "Payment System"]

view_mapping = {"Garden": 1, "Street": 2, "Apartment": 3, "Apartment Building": 4}
facing_mapping = {"North": 1, "South": 2}
elevator_mapping = {"Yes": 1, "No": 0}
payment_mapping = {"Cash": 0, "Installments": 1}

# Streamlit Page Config
st.set_page_config(page_title="🏠 House Price Prediction", layout="centered")

st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #89f7fe, #66a6ff);
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# App Title
st.markdown('<h1>🏠 House Price Prediction</h1>', unsafe_allow_html=True)
st.markdown('<p>Enter the details to predict house price in Egypt.</p>', unsafe_allow_html=True)

# Input Widgets
area = st.slider("📏 Area (sqm)", 90, 250, step=10)
bedroom = st.number_input("🛏 Bedroom", min_value=0, step=1)
bathroom = st.number_input("🚻 Bathroom", min_value=0, step=1)
floor = st.number_input("🏢 Floor", min_value=0, step=1)
view = st.radio("🌄 View", list(view_mapping.keys()))
facing = st.radio("🧭 Facing", list(facing_mapping.keys()))
elevator = st.radio("🚪 Elevator", ["Yes", "No"])
payment = st.radio("💰 Payment System", ["Cash", "Installments"])

# Prediction function
def predict_price(area, bedroom, bathroom, floor, view, facing, elevator, payment):
    location = location_mapping.get(location, 0)
    view = view_mapping.get(view, 0)
    facing = facing_mapping.get(facing, 0)
    elevator = elevator_mapping.get(elevator, 0)
    payment = payment_mapping.get(payment, 0)
    
    input_data = np.array([[area, bedroom, bathroom, floor, view, facing, elevator, payment]])
    input_df = pd.DataFrame(input_data, columns=feature_columns)
    
    predicted_price = model.predict(input_df)[0]
    return predicted_price

# Buttons
if st.button("Predict Price"):
    result = predict_price(area, bedroom, bathroom, floor, view, facing, elevator, payment)
    st.success(f"💰 Predicted House Price: {result:,.2f} EGP")

if st.button('Clear'):
    st.rerun()
