import streamlit as st
import pickle
import numpy as np

# Load the trained model
pkl_filename = "sales_prediction_model.pkl"
with open(pkl_filename, 'rb') as file:
    model = pickle.load(file)

# Define a function to predict sales
def predict_sales(outlet_type, outlet_identifier_out027, item_mrp, outlet_identifier_out019, outlet_age, outlet_identifier_out035):
    features = np.array([[outlet_type, outlet_identifier_out027, item_mrp, outlet_identifier_out019, outlet_age, outlet_identifier_out035]])
    prediction = model.predict(features)
    return prediction[0]

# Streamlit app
st.title("Sales Prediction App")
st.markdown("""
<style>
    .reportview-container {
        background: #f0f0f5;
        color: #333;
    }
    .sidebar .sidebar-content {
        background: #f8f9fa;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
</style>
""", unsafe_allow_html=True)

st.header("Enter the details to predict sales:")

# User inputs
outlet_type = st.selectbox("Outlet Type", options=[0, 1, 2, 3])
outlet_identifier_out027 = st.selectbox("Outlet Identifier OUT027", options=[0, 1])
item_mrp = st.number_input("Item MRP", min_value=0.0, format="%.2f")
outlet_identifier_out019 = st.selectbox("Outlet Identifier OUT019", options=[0, 1])
outlet_age = st.number_input("Outlet Age", min_value=0, max_value=100, step=1)
outlet_identifier_out035 = st.selectbox("Outlet Identifier OUT035", options=[0, 1])

if st.button("Predict Sales"):
    result = predict_sales(outlet_type, outlet_identifier_out027, item_mrp, outlet_identifier_out019, outlet_age, outlet_identifier_out035)
    st.success(f"The predicted sales are: ${result:.2f}")

# Footer
st.markdown("""
<footer style='text-align: center; padding: 20px;'>
    &copy; 2024 Sales Prediction App. All rights reserved.
</footer>
""", unsafe_allow_html=True)
