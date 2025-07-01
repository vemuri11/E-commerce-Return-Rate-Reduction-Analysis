import streamlit as st
import pandas as pd
import joblib
import os

st.title("📦 E-commerce Return Prediction")

# Load model
model_path = os.path.join(os.path.dirname(__file__), "..", "models", "return_predictor.pkl")
model = joblib.load(model_path)

st.markdown("This tool predicts whether a product will be **returned** based on order features.")

# Input fields
quantity = st.number_input("Enter Quantity", min_value=1, step=1)
unit_price = st.number_input("Enter Unit Price", min_value=0.0, step=0.1)

# Total price is auto-calculated
total_price = quantity * unit_price
st.write(f"Total Price: ₹ {total_price:.2f}")

# Predict button
if st.button("Predict Return"):
    input_df = pd.DataFrame([[quantity, unit_price, total_price]],
                            columns=["Quantity", "UnitPrice", "TotalPrice"])
    prediction = model.predict(input_df)[0]

    if prediction == 1:
        st.error("🔁 This product is likely to be **Returned**.")
    else:
        st.success("✅ This product is **not likely to be returned.**")