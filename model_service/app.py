from flask import Flask, request, jsonify
import joblib
import os
import time

app = Flask(__name__)

MODEL_PATH = os.getenv("MODEL_PATH", "/data/model.pkl")

# Modell beim Start laden (wichtig!)
try:
    model = joblib.load(MODEL_PATH)
    model_loaded = True
except Exception as e:
    model_loaded = False
    load_error = str(e)

@app.route("/health")
def health():
    if model_loaded:
        return jsonify({
            "status": "healthy",
            "model": "loaded"
        }), 200
    else:
        return jsonify({
            "status": "unhealthy",
            "error": load_error
        }), 500


@app.route("/predict", methods=["POST"])
def predict():
    if not model_loaded:
        return jsonify({"error": "Model not loaded"}), 500

    data = request.get_json()

    if "features" not in data:
        return jsonify({"error": "Missing 'features'"}), 400

    features = data["features"]

    prediction = model.predict([features])

    return jsonify({
        "prediction": prediction[0],
        "timestamp": time.time()
    })