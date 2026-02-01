# Diabetes Shield - AI-Powered Diabetes Risk Assessment

![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.8%2B-green)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28-red)
![Contributions](https://img.shields.io/badge/contributions-welcome-brightgreen)

A machine learning-powered web application that assesses diabetes risk based on lifestyle factors, providing personalized prevention strategies. Analyzes CDC data from 253,680 Americans to predict diabetes risk and offer actionable health recommendations.

##  Live Demo

[![Try Diabetes Shield](https://img.shields.io/badge/TRY_LIVE_DEMO-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://bamideleadedeji-diabetes-shield.streamlit.app/)


##  Features

###  Risk Assessment
- **Personalized Risk Score** based on BMI, age, lifestyle factors
- **Interactive Gauge** with color-coded risk levels (Low/Medium/High)
- **Comparative Analysis** showing how you compare to average population

###  Action Plans
- **Customized Recommendations** tailored to your risk level
- **4-Week Starter Challenge** with weekly achievable goals
- **Progress Tracking** to monitor health improvements

###  Education & Tools
- **BMI Calculator** with healthy range guidance
- **Myth vs Fact** debunking common diabetes misconceptions
- **Evidence-Based Tips** backed by CDC research

##  Quick Start

### Option 1: Web Version (Recommended)
Simply visit the live demo link above!

### Option 2: Local Installation
```bash
# 1. Clone repository
git clone https://github.com/bamideleadedeji/diabetes-shield.git
cd diabetes-shield

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run application
streamlit run app.py

# 4. Open browser: http://localhost:8501

# Open diabetes_shield_simple.html in any browser - works immediately!

Project Structure
diabetes-shield/
├── app.py                    # Main Streamlit application
├── diabetes_model.py         # ML model and risk calculation
├── diabetes_shield_simple.html  # HTML version (no installation)
├── simple_diabetes.py        # Command-line interface
├── images/                   # Professional graphics
│   ├── screenshot-dashboard.png
│   ├── architecture-diagram.png
│   └── impact-infographic.png
├── requirements.txt          # Python dependencies
├── LICENSE                   # MIT License
└── README.md                 # This file

Technology Stack
Backend: Python 3.8+, Scikit-learn, Pandas, NumPy

Frontend: Streamlit, Plotly for interactive visualizations

Deployment: Streamlit Cloud, Docker-compatible

Data Source: CDC Diabetes Health Indicators (UCI Repository ID: 891)

How It Works
1. Data Analysis
Analyzed 253,680 CDC health records

Identified key risk factors: BMI (25%), Age (15%), Physical Activity (10%)

Trained Random Forest model with 83% ROC-AUC accuracy

2. Risk Calculation
Input: BMI, age, blood pressure, lifestyle habits

Processing: Machine learning model predicts risk probability

Output: Personalized risk score (0-100%) with actionable recommendations

3. Prevention Strategies
Low Risk (<30%): Maintenance and regular check-ups

Medium Risk (30-60%): Lifestyle improvements and monitoring

High Risk (>60%): Medical consultation and active intervention

 Public Health Impact
Key Statistics:
537 million people have diabetes worldwide

85% of type 2 diabetes cases are preventable

58% risk reduction with 5-10% weight loss

$9,600 annual savings per prevented case

Prevention Benefits:
Weight Management: 5-10% loss = 50% risk reduction

Regular Exercise: 150 mins/week = 46% risk reduction

Healthy Diet: More fruits/vegetables = 20-30% risk reduction

Early Detection: Can prevent or delay diabetes onset

 Project Visualizations
Dashboard Interface
https://images/screenshot-dashboard.png

System Architecture
https://images/architecture-diagram.png

Public Health Impact
https://images/impact-infographic.png

 Deployment Options

# https://bamideleadedeji-diabetes-shield.streamlit.app/
2. Docker (For Developers)
dockerfile
# Build and run anywhere
docker build -t diabetes-shield .
docker run -p 8501:8501 diabetes-shield
3. Local Network (For Clinics/Organizations)
bash
# Share within your organization
streamlit run app.py --server.address 0.0.0.0
 Contributing
We welcome contributions to improve public health impact!

Ways to Contribute:
Improve Model Accuracy - Add more risk factors

Enhance UI/UX - Make it more accessible

Add Translations - Reach non-English speakers

Documentation - Improve guides and tutorials

Contribution Process:
bash
1. Fork the repository
2. Create feature branch
3. Make improvements
4. Submit pull request
 Important Disclaimer
This tool is for educational and informational purposes only.

NOT medical advice: Always consult healthcare professionals for medical decisions.

Not a diagnosis: This tool assesses risk, not diagnoses diabetes.

Data privacy: We don't store personal health information.

 License
This project is licensed under the MIT License - see the LICENSE file for details.

 Acknowledgments
Centers for Disease Control (CDC) - For public health data

UCI Machine Learning Repository - For curated dataset

Streamlit - For amazing open-source framework

Open Source Community - For libraries and tools

 Contact & Support
GitHub Issues: Report bugs or request features

Email: bamideleadedeji2000@gmail.com

LinkedIn:  https://www.linkedin.com/in/adedeji-bamidele-88a159263/

 Join Our Mission
Help us reach 1 million people with diabetes prevention education!

Share this project:

On LinkedIn as a portfolio piece

With friends and family for health awareness

In community health programs

With healthcare providers for patient education

<div align="center"> <h3>Made with  for a healthier world</h3> <p>Every life saved from diabetes is a victory for humanity</p>
 Star this repo if you find it useful!

</div> ```


