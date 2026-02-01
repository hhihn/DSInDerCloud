FROM python:3.11-slim

# Systemabhängigkeiten (für pandas / sklearn realistisch)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Arbeitsverzeichnis = Kedro-Projekt-Root
WORKDIR /app

# Python Dependencies installieren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kedro-Projekt kopieren
COPY . .

# WICHTIG: src/ ins PYTHONPATH aufnehmen
ENV PYTHONPATH=/app/src

# Optional: saubere Logs
ENV PYTHONUNBUFFERED=1

# Default: Kedro Pipeline ausführen
CMD ["kedro", "run", "--pipeline", "churn"]