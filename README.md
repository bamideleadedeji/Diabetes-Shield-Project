Diabetes ShieldDiabetes Shield is a predictive health tool designed to help users assess their risk of developing diabetes based on key health metrics like BMI, age, and blood pressure. Live ApplicationYou can access the interactive version of this project here:https://diabetes-shield-project-gdl7pgivucqn2fa7dnlgom.streamlit.app/ How It WorksThe calculator uses a simplified risk assessment model based on the following logic:Body Mass Index (BMI): Calculated using height and weight.$BMI = \frac{weight(kg)}{height(m)^2}$Risk Factors:High BMI: Increases risk significantly if over 25 or 30.Age: Increased risk for individuals over 55.Blood Pressure: Adds weight to the risk score if hypertension is present.Risk LevelsRisk ScoreLevelRecommendation< 30%LOWKeep up the good work!30% - 60%MEDIUMConsider lifestyle improvements.> 60%HIGHConsult with a doctor. Local InstallationIf you want to run this project on your own machine, follow these steps:1. Clone the RepositoryBashgit clone https://github.com/Ybamideleadedeji/Diabetes-Sheild-Project.git
cd YOUR_REPO_NAME
2. Set Up a Virtual Environment (Recommended)Bash# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
3. Install DependenciesMake sure you have a requirements.txt file in your folder.Bashpip install -r requirements.txt
4. Run the AppBashstreamlit run app.py
Project Structureapp.py: The main Streamlit application code.requirements.txt: List of Python libraries needed (Streamlit, Pandas, etc.).README.md: Project documentation.
