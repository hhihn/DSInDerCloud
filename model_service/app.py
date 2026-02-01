from flask import Flask, request, jsonify
import joblib
import os

app = Flask(__name__)


# Modell beim Start laden
try:
    model = joblib.load(MODEL_PATH)
    model_loaded = True
except Exception as e:
    model_loaded = False
    load_error = str(e)

@app.route("/health")
def health():
    if model_loaded:
        return jsonify({"status": "healthy", "model": "loaded"}), 200
    else:
        return jsonify({"status": "unhealthy", "error": load_error}), 500

@app.route("/predict", methods=["POST"])
def predict():
    pass

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)