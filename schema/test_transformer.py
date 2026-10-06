from schema import SalaryPredictionInput
from transformer import transform_input


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


print("Validated input:")
print(data)

print("\nModel-ready data:")

model_input = transform_input(data)

print(model_input)