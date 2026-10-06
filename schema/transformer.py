import pandas as pd

from schema.schema import SalaryPredictionInput


# =========================================================
# EXACT FEATURE ORDER USED BY THE TRAINING DATA
# =========================================================

MODEL_COLUMNS = [

    # Job title
    "job_title_AI Engineer",
    "job_title_Analytics Engineer",
    "job_title_Business Intelligence Analyst",
    "job_title_Computer Vision Engineer",
    "job_title_Data Analyst",
    "job_title_Data Engineer",
    "job_title_Data Science Manager",
    "job_title_Data Scientist",
    "job_title_LLM Engineer",
    "job_title_MLOps Engineer",
    "job_title_Machine Learning Engineer",
    "job_title_Research Scientist",

    # Experience level
    "Entry(0-2)",
    "Mid(2-5)",
    "Senior",
    "Lead",
    "Executive",

    # Employment type
    "employment_type_Contract",
    "employment_type_Freelance",
    "employment_type_Full-time",
    "employment_type_Part-time",

    # Company location
    "company_location_AU",
    "company_location_BR",
    "company_location_CA",
    "company_location_DE",
    "company_location_ES",
    "company_location_FR",
    "company_location_GB",
    "company_location_IN",
    "company_location_NL",
    "company_location_PL",
    "company_location_SG",
    "company_location_US",

    # Industry
    "industry_Consulting",
    "industry_Education",
    "industry_Energy",
    "industry_Finance",
    "industry_Government",
    "industry_Healthcare",
    "industry_Manufacturing",
    "industry_Media",
    "industry_Retail",
    "industry_Technology",

    # Employee residence
    "employee_residence_IN",

    # Encoded features
    "education_level",
    "company_size",

    # Scaled numerical feature
    "years_experience"
]


# =========================================================
# ENCODING MAPS
# =========================================================

EDUCATION_MAPPING = {
    "Bootcamp": 0,
    "Self-taught": 1,
    "Bachelors": 2,
    "Masters": 3,
    "PhD": 4
}


COMPANY_SIZE_MAPPING = {
    "S": 0,
    "M": 1,
    "L": 2
}


# =========================================================
# TRANSFORMATION FUNCTION
# =========================================================

def transform_input(data: SalaryPredictionInput) -> pd.DataFrame:

    # -----------------------------------------------------
    # Start with all model columns as 0
    # -----------------------------------------------------

    features = {
        column: 0
        for column in MODEL_COLUMNS
    }


    # -----------------------------------------------------
    # JOB TITLE
    # -----------------------------------------------------

    job_column = f"job_title_{data.job_title}"

    features[job_column] = 1


    # -----------------------------------------------------
    # EXPERIENCE LEVEL
    # -----------------------------------------------------

    experience_column = data.experience_level

    if data.experience_level == "Entry":
        experience_column = "Entry(0-2)"

    elif data.experience_level == "Mid":
        experience_column = "Mid(2-5)"

    features[experience_column] = 1


    # -----------------------------------------------------
    # EMPLOYMENT TYPE
    # -----------------------------------------------------

    employment_column = (
        f"employment_type_{data.employment_type}"
    )

    features[employment_column] = 1


    # -----------------------------------------------------
    # COMPANY LOCATION
    # -----------------------------------------------------

    location_column = (
        f"company_location_{data.company_location}"
    )

    features[location_column] = 1


    # -----------------------------------------------------
    # INDUSTRY
    # -----------------------------------------------------

    industry_column = (
        f"industry_{data.industry}"
    )

    features[industry_column] = 1


    # -----------------------------------------------------
    # EMPLOYEE RESIDENCE
    # -----------------------------------------------------

    if data.employee_residence == "IN":
        features["employee_residence_IN"] = 1


    # -----------------------------------------------------
    # EDUCATION LEVEL
    # -----------------------------------------------------

    features["education_level"] = EDUCATION_MAPPING[
        data.education_level
    ]


    # -----------------------------------------------------
    # COMPANY SIZE
    # -----------------------------------------------------

    features["company_size"] = COMPANY_SIZE_MAPPING[
        data.company_size
    ]


    # -----------------------------------------------------
    # YEARS EXPERIENCE
    # -----------------------------------------------------

    features["years_experience"] = (
        data.scaled_years_experience
    )


    # -----------------------------------------------------
    # Convert dictionary → DataFrame
    # -----------------------------------------------------

    df = pd.DataFrame(
        [features],
        columns=MODEL_COLUMNS
    )

    return df