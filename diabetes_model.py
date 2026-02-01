
import numpy as np

class DiabetesPredictor:
    def __init__(self, model_path="diabetes_model.pkl"):
        self.model = None
    
    def predict_risk(self, user_data):
        bmi = user_data.get("BMI", 25)
        age = user_data.get("Age", 5)
        high_bp = user_data.get("HighBP", 0)
        
        base_risk = 0.15
        
        if bmi > 30:
            base_risk += 0.3
        elif bmi > 25:
            base_risk += 0.15
        
        if age > 8:
            base_risk += 0.2
        
        if high_bp == 1:
            base_risk += 0.15
        
        base_risk = min(0.9, base_risk)
        
        if base_risk < 0.3:
            risk_level = "Low"
        elif base_risk < 0.6:
            risk_level = "Medium"
        else:
            risk_level = "High"
        
        return {
            "risk_score": float(base_risk),
            "risk_level": risk_level,
            "risk_percentage": f"{base_risk * 100:.1f}%"
        }
    
    def get_recommendations(self, risk_score):
        if risk_score < 0.3:
            return {
                "level": "Low Risk",
                "message": "Great job! Keep maintaining your healthy lifestyle.",
                "actions": [
                    "Continue regular exercise",
                    "Maintain balanced diet",
                    "Annual health check-ups"
                ]
            }
        elif risk_score < 0.6:
            return {
                "level": "Medium Risk",
                "message": "Some improvements can help reduce your risk.",
                "actions": [
                    "Increase physical activity",
                    "Eat more vegetables",
                    "Monitor blood pressure"
                ]
            }
        else:
            return {
                "level": "High Risk",
                "message": "Take action now to prevent diabetes.",
                "actions": [
                    "Consult with a doctor",
                    "Lose weight if needed",
                    "Daily exercise",
                    "Healthy eating"
                ]
            }

def calculate_bmi(height_feet, height_inches, weight_lbs):
    height_m = (height_feet * 12 + height_inches) * 0.0254
    weight_kg = weight_lbs * 0.453592
    
    if height_m > 0:
        bmi = weight_kg / (height_m ** 2)
    else:
        bmi = 22
    
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    
    return round(bmi, 1), category
