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
    if not model_loaded:
        return jsonify({"error": "model not loaded"}), 500

    data = request.get_json()
    features = data.get("features")

    if features is None:
        return jsonify({"error": "missing features"}), 400

    prediction = model.predict([features])
    return jsonify({"prediction": int(prediction[0])})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)