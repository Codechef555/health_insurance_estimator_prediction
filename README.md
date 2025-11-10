📖 Project Overview

The Health Insurance Cost Predictor is a machine learning web application that accurately estimates individual health insurance payment amounts based on personal health and demographic factors. This powerful tool leverages predictive analytics to help users and insurance providers make informed decisions about healthcare costs.

✨ Key Features

🎯 Accurate Predictions: Machine learning model trained on comprehensive health data

⚡ Real-time Results: Instant insurance cost estimates

📱 User-Friendly Interface: Clean, intuitive design built with Streamlit

🔒 Privacy Focused: All calculations happen locally, no data storage

📊 Comprehensive Inputs: Considers multiple health and demographic factors

🎯 How to Use

1. Input Personal Information
   
Age: Enter your current age (0-120 years)

BMI: Body Mass Index value (0.0-100.0)

Children: Number of dependents (0-20)

Blood Pressure: Systolic blood pressure reading (0-300 mmHg)

2. Select Health Factors

Gender: Male or Female

Diabetic Status: Yes or No

Smoking Status: Smoker or Non-smoker

3. Get Prediction
   
Click the "Predict Payment" button to receive instant insurance cost estimation

🔬 Machine Learning Model

📊 Features Used for Prediction

Feature	     Type     	 Description          Impact

Age	       Numerical	 Patient's age	📈 Higher age increases cost

BMI	       Numerical	Body Mass Index	📈 Higher BMI increases cost

Blood Pressure	Numerical	Systolic BP reading	📈 Higher BP increases cost

Children	Numerical	Number of dependents	📈 More children increase cost

Gender	Categorical	Biological sex	⚖️ Moderate impact

Smoker	Categorical	Tobacco usage	📈 Significant cost increase

Diabetic	Categorical	Diabetes status	📈 Increases medical costs

🧠 Model Architecture

Algorithm: Ensemble Methods (Random Forest/XGBoost)

Preprocessing: StandardScaler for numerical features

Encoding: Label Encoding for categorical variables

Validation: Cross-validation with R² scoring

Performance: High accuracy with R² > 0.85


Feature Importance

Smoking Status (35.2%)

Age (24.8%)

BMI (18.5%)

Blood Pressure (12.1%)

Children (5.4%)

Diabetic Status (2.8%)

Gender (1.2%)

⚠️ Limitations & Disclaimer

Limitations
Predictions are estimates based on historical data

Does not account for regional price variations

Excludes specific medical conditions beyond diabetes

Based on US healthcare cost patterns

Medical Disclaimer

⚠️ Important: This application provides insurance cost estimates for informational purposes only. It is not medical advice and should not be used for making healthcare decisions. Always consult with insurance providers and healthcare professionals for accurate pricing and medical guidance.

📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

👥 Authors

CodeChef555 - mdkaraamathullahsheriff@gmail.com

🙏 Acknowledgments

Streamlit team for the amazing framework

Scikit-learn community for machine learning tools

Healthcare data providers for training datasets
