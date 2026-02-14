
import streamlit as st
import plotly.graph_objects as go
from diabetes_model import DiabetesPredictor, calculate_bmi

st.set_page_config(
    page_title="Diabetes Shield",
    page_icon="",
    layout="wide"
)

st.markdown("""
<style>
    .main-title {
        text-align: center;
        color: #1E3A8A;
        font-size: 2.5rem;
    }
    .card {
        background-color: #F8FAFC;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-title"> Diabetes Shield</h1>', unsafe_allow_html=True)
st.write("Simple diabetes risk assessment tool")

predictor = DiabetesPredictor()

with st.sidebar:
    st.header("Your Health Profile")

    age = st.slider("Age", 18, 100, 35)

    col1, col2 = st.columns(2)
    with col1:
        height_feet = st.selectbox("Height (feet)", [4, 5, 6, 7], index=1)
    with col2:
        height_inches = st.selectbox("Height (inches)", list(range(12)), index=8)

    weight_lbs = st.slider("Weight (lbs)", 80, 350, 160)

    bmi, bmi_category = calculate_bmi(height_feet, height_inches, weight_lbs)
    st.metric("Your BMI", f"{bmi} ({bmi_category})")

    st.subheader("Health Conditions")
    high_bp = st.checkbox("High Blood Pressure")
    high_chol = st.checkbox("High Cholesterol")
    smoker = st.checkbox("Smoker")

    st.subheader("Lifestyle")
    exercise = st.select_slider(
        "Weekly Exercise",
        options=["None", "1-2 hours", "3-4 hours", "5+ hours"],
        value="1-2 hours"
    )

    calculate_btn = st.button("Calculate My Risk", type="primary")

if calculate_btn:
    user_data = {
        "BMI": bmi,
        "Age": min(13, (age - 18) // 5),
        "HighBP": 1 if high_bp else 0,
        "HighChol": 1 if high_chol else 0,
        "Smoker": 1 if smoker else 0,
        "PhysActivity": 1 if exercise != "None" else 0
    }

    result = predictor.predict_risk(user_data)
    recommendations = predictor.get_recommendations(result["risk_score"])

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Risk Level", result["risk_level"])

    with col2:
        st.metric("Risk Score", result["risk_percentage"])

    with col3:
        st.metric("Recommendation", recommendations["level"])

    st.subheader("Risk Assessment")
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=result["risk_score"] * 100,
        title={"text": "Diabetes Risk Meter"},
        gauge={
            "axis": {"range": [0, 100]},
            "steps": [
                {"range": [0, 25], "color": "green"},
                {"range": [25, 50], "color": "yellow"},
                {"range": [50, 100], "color": "red"}
            ]
        }
    ))
    st.plotly_chart(fig)

    st.subheader("Your Action Plan")
    st.write(recommendations["message"])

    for i, action in enumerate(recommendations["actions"], 1):
        st.write(f"{i}. {action}")

    with st.expander(" Learn More About Diabetes Prevention"):
        st.write("""
        **Key Facts:**
        - 37 million Americans have diabetes
        - 96 million have prediabetes
        - BMI is the #1 predictor of diabetes risk
        - Exercise can reduce risk by up to 58%

        **Prevention Tips:**
        1. Maintain healthy weight
        2. Exercise regularly
        3. Eat more vegetables
        4. Get regular check-ups
        """)
else:
    st.info(" Fill out your health profile and click 'Calculate My Risk'")

st.markdown("---")
st.caption("This tool is for educational purposes. Always consult healthcare professionals for medical advice.")
