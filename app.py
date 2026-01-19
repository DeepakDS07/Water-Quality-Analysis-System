import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

model = joblib.load("model.pkl")
le = joblib.load("label_encoder.pkl")

st.set_page_config(page_title="Water Quality Analyzer", layout="centered")

st.title("💧 AI-Based Water Quality Analysis System")
st.write("Analyze water quality using chemical parameters")

st.sidebar.header("Enter Water Parameters")

pH = st.sidebar.slider("pH", 5.5, 9.5, 7.0)
TDS = st.sidebar.number_input("TDS (mg/L)", 0, 3000, 400)
Hardness = st.sidebar.number_input("Hardness (mg/L)", 0, 800, 200)
Turbidity = st.sidebar.slider("Turbidity (NTU)", 0.0, 10.0, 3.0)
Nitrate = st.sidebar.number_input("Nitrate (mg/L)", 0, 100, 10)
Chloride = st.sidebar.number_input("Chloride (mg/L)", 0, 600, 150)

if st.button("Analyze Water Quality"):
    input_data = pd.DataFrame([{
        "pH": pH,
        "TDS": TDS,
        "Hardness": Hardness,
        "Turbidity": Turbidity,
        "Nitrate": Nitrate,
        "Chloride": Chloride
    }])

    prediction = model.predict(input_data)
    result = le.inverse_transform(prediction)[0]

    if result == "Safe":
        st.success("🟢 Water Quality: SAFE")
    elif result == "Moderate":
        st.warning("🟡 Water Quality: MODERATE")
    else:
        st.error("🔴 Water Quality: UNSAFE")

    # Parameter comparison chart
    limits = {
        "pH": 8.5,
        "TDS": 500,
        "Hardness": 300,
        "Turbidity": 5,
        "Nitrate": 10,
        "Chloride": 250
    }

    fig, ax = plt.subplots()
    ax.bar(input_data.columns, input_data.iloc[0], label="Actual Value")
    ax.plot(limits.keys(), limits.values(), color="red", marker="o", label="Safe Limit")
    ax.set_ylabel("Value")
    ax.set_title("Water Parameters vs Safe Limits")
    ax.legend()

    st.pyplot(fig)

    st.subheader("🌱 Sustainability Insight")
    if Nitrate > 10:
        st.write("- High nitrate may indicate fertilizer runoff.")
    if TDS > 500:
        st.write("- High TDS can affect taste and long-term health.")
    if Turbidity > 5:
        st.write("- High turbidity may support microbial growth.")
