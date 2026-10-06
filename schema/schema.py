from typing import Literal
from pydantic import BaseModel, Field, computed_field


class SalaryPredictionInput(BaseModel):

    job_title: Literal[
        "AI Engineer",
        "Analytics Engineer",
        "Business Intelligence Analyst",
        "Computer Vision Engineer",
        "Data Analyst",
        "Data Engineer",
        "Data Science Manager",
        "Data Scientist",
        "LLM Engineer",
        "MLOps Engineer",
        "Machine Learning Engineer",
        "Research Scientist"
    ]

    experience_level: Literal[
        "Entry",
        "Mid",
        "Senior",
        "Lead",
        "Executive"
    ]

    employment_type: Literal[
        "Contract",
        "Freelance",
        "Full-time",
        "Part-time"
    ]

    company_location: Literal[
        "AU",
        "BR",
        "CA",
        "DE",
        "ES",
        "FR",
        "GB",
        "IN",
        "NL",
        "PL",
        "SG",
        "US"
    ]

    industry: Literal[
        "Consulting",
        "Education",
        "Energy",
        "Finance",
        "Government",
        "Healthcare",
        "Manufacturing",
        "Media",
        "Retail",
        "Technology"
    ]

    employee_residence: Literal["IN"]

    education_level: Literal[
        "Bootcamp",
        "Self-taught",
        "Bachelors",
        "Masters",
        "PhD"
    ]

    company_size: Literal[
        "S",
        "M",
        "L"
    ]

    years_experience: float = Field(
        ge=0,
        le=50,
        description="Years of professional experience"
    )

    @computed_field
    @property
    def scaled_years_experience(self) -> float:

        mean = 8.36144
        scale = 4.82032583

        return (self.years_experience - mean) / scale