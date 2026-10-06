from schema import SalaryPredictionInput


data = SalaryPredictionInput(
    job_title="Software Developer",
    experience_level="Senior",
    employment_type="Full-time",
    company_location="US",
    industry="Technology",
    employee_residence="IN",
    education_level="Masters",
    company_size="L",
    years_experience=6
)


print(data)