import joblib

from schema import SalaryPredictionInput
from transformer import transform_input


# Load trained model
model = joblib.load(
    "model/salary_prediction_model.pkl"
)


# API-like input
data = SalaryPredictionInput(
    job_title="Data Scientist",
    experience_level="Senior",
    employment_type="Full-time",
    company_location="US",
    industry="Technology",
    employee_residence="IN",
    education_level="Masters",
    company_size="L",
    years_experience=6
)


# Transform input
model_input = transform_input(data)


# Prediction
prediction = model.predict(model_input)


print("Predicted salary:", prediction[0])