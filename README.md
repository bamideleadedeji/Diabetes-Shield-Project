
<!DOCTYPE html>
<html>
<head>
    <title>Diabetes Shield - Simple Version</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 600px; margin: 40px auto; padding: 20px; }
        .card { background: #f8f9fa; border-left: 5px solid #007bff; padding: 20px; margin: 20px 0; }
        button { background: #007bff; color: white; border: none; padding: 10px 20px; cursor: pointer; }
        .result { font-size: 24px; font-weight: bold; margin: 20px 0; }
    </style>
</head>
<body>
    <h1>Diabetes Shield</h1>
    <p>Simple Diabetes Risk Calculator</p>
    
    <div class="card">
        <h3>Your Health Information:</h3>
        <p>Height: <input type="number" id="height" value="5"> feet 
           <input type="number" id="inches" value="8"> inches</p>
        <p>Weight: <input type="number" id="weight" value="160"> lbs</p>
        <p>Age: <input type="number" id="age" value="35"> years</p>
        <p><input type="checkbox" id="highbp"> High Blood Pressure</p>
        <button onclick="calculateRisk()">Calculate Risk</button>
    </div>
    
    <div id="result" class="card" style="display:none;">
        <h3>Your Results:</h3>
        <p id="bmi" class="result"></p>
        <p id="risk" class="result"></p>
        <p id="recommendation"></p>
    </div>
    
    <script>
    function calculateRisk() {
        // Get values
        const heightFeet = parseFloat(document.getElementById('height').value);
        const heightInches = parseFloat(document.getElementById('inches').value);
        const weightLbs = parseFloat(document.getElementById('weight').value);
        const age = parseFloat(document.getElementById('age').value);
        const highBP = document.getElementById('highbp').checked;
        
        // Calculate BMI
        const heightM = (heightFeet * 12 + heightInches) * 0.0254;
        const weightKg = weightLbs * 0.453592;
        const bmi = weightKg / (heightM * heightM);
        
        // Calculate risk
        let risk = 0.15;
        if (bmi > 30) risk += 0.3;
        else if (bmi > 25) risk += 0.15;
        
        if (age > 55) risk += 0.2;
        if (highBP) risk += 0.15;
        
        risk = Math.min(risk, 0.9);
        
        // Determine risk level
        let riskLevel, recommendation;
        if (risk < 0.3) {
            riskLevel = "LOW";
            recommendation = "Keep up the good work!";
        } else if (risk < 0.6) {
            riskLevel = "MEDIUM";
            recommendation = "Consider lifestyle improvements.";
        } else {
            riskLevel = "HIGH";
            recommendation = "Consult with a doctor.";
        }
        
        // Show results
        document.getElementById('bmi').textContent = `BMI: ${bmi.toFixed(1)}`;
        document.getElementById('risk').textContent = `Risk: ${(risk*100).toFixed(1)}% (${riskLevel})`;
        document.getElementById('recommendation').textContent = recommendation;
        document.getElementById('result').style.display = 'block';
    }
    </script>
</body>
</html>
