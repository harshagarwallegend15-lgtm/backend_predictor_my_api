FROM python:3.13.9-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Backend API only
COPY app/api_design.py ./app/api_design.py

# Schema and transformation logic
COPY schema/__init__.py ./schema/__init__.py
COPY schema/schema.py ./schema/schema.py
COPY schema/transformer.py ./schema/transformer.py

# Trained model
COPY model/salary_prediction_model.pkl ./model/salary_prediction_model.pkl

EXPOSE 8000

CMD ["uvicorn", "app.api_design:app", "--host", "0.0.0.0", "--port", "8000"]