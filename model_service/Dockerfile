FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /app/data

COPY app.py .
COPY data/churn_model.pkl /app/data/churn_model.pkl

EXPOSE 5000
CMD ["python", "app.py"]