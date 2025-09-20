import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go

# ----------------------
# Load the trained pipeline
# ----------------------
try:
    loaded_pipeline = joblib.load("Loan_approval_fullpipeline.joblib")

except FileNotFoundError:
    st.error("❌ The 'Loan_approval_fullpipeline.joblib' file was not found.")
    st.stop()

# ----------------------
# Page setup
# ----------------------
st.set_page_config(page_title="🏡 Loan Approval Predictor", layout="centered")

# ----------------------
# App Title
# ----------------------
st.title("🏡 Loan Approval Predictor")
st.markdown("### Enter applicant details and financials below. The app will predict the loan approval outcome with a likelihood gauge.")

# ----------------------
# Applicant Details
# ----------------------
st.header("👤 Applicant Details")
col1, col2 = st.columns(2)
with col1:
    education = st.selectbox("📘 Education", ["Graduate", "Not Graduate"])
with col2:
    self_employed = st.selectbox("💼 Self Employed", ["Yes", "No"])

# ----------------------
# Financial Info
# ----------------------
st.header("💰 Financial Information")
col1, col2 = st.columns(2)
with col1:
    no_of_dependents = st.slider("👨‍👩‍👧 Number of Dependents", 0, 10, 1)
    income_annum = st.number_input("💵 Annual Income (Rs)", min_value=0.0, step=10000.0, value=8700000.0)
    loan_amount = st.number_input("🏦 Loan Amount (Rs)", min_value=0.0, step=10000.0, value=28300000.0)
    loan_term = st.slider("📅 Loan Term (months)", 1, 72, 12)
with col2:
    cibil_score = st.slider("📊 CIBIL Score", 300, 900, 499)
    residential_assets_value = st.number_input("🏠 Residential Assets Value (Rs)", min_value=0.0, step=10000.0, value=20400000.0)
    commercial_assets_value = st.number_input("🏢 Commercial Assets Value (Rs)", min_value=0.0, step=10000.0, value=13600000.0)
    luxury_assets_value = st.number_input("🚗 Luxury Assets Value (Rs)", min_value=0.0, step=10000.0, value=27900000.0)
    bank_asset_value = st.number_input("🏦 Bank Asset Value (Rs)", min_value=0.0, step=10000.0, value=10200000.0)


# ----------------------
# Prediction
# ----------------------
if st.button("🔮 Predict Loan Approval"):
    input_data = pd.DataFrame({
        " no_of_dependents": [no_of_dependents],
        " income_annum": [income_annum],
        " loan_amount": [loan_amount],
        " loan_term": [loan_term],
        " cibil_score": [cibil_score],
        " residential_assets_value": [residential_assets_value],
        " commercial_assets_value": [commercial_assets_value],
        " luxury_assets_value": [luxury_assets_value],
        " bank_asset_value": [bank_asset_value],
        " education": [education],
        " self_employed": [self_employed],
    })

    try:
        prediction = loaded_pipeline.predict(input_data)[0]

        st.subheader("📊 Prediction Result")
        if prediction == 0:
            st.success("✅ Loan Approved! Congratulations! 🎉")
        else:
            st.error("❌ Loan Not Approved. Please review your application.")

    except Exception as e:
        st.error(f"⚠️ An error occurred during prediction: {e}")
