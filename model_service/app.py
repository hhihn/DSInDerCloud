from flask import Flask, request, jsonify
import joblib
import os

app = Flask(__name__)

# lade den model path aus der umgebungsvariablen "MODEL_PATH"
# diese wird über kubernetes zur verfügung gestellt und ist
# nur im container gesetzt
MODEL_PATH = os.getenv("MODEL_PATH", "/data/churn_model.pkl")

# Modell beim Start laden
try:
    model = joblib.load(MODEL_PATH)
    model_loaded = True
except Exception as e:
    model_loaded = False
    load_error = str(e)

# der health point wird von kubernetes genutzt um zu checken ob er container noch
# läuft oder ob schon ein restart notwendig ist
@app.route("/health")
def health():
    if model_loaded:
        return jsonify({"status": "healthy", "model": "loaded"}), 200
    else:
        return jsonify({"status": "unhealthy", "error": load_error}), 500

# diese methode stellt die api zur vorhersage bereit
# da gehen meine daten rein und kommt ein output (vorhersage ja/nein) raus
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    features = data.get("features")

    if features is None:
        return jsonify({"status": "unavailable", "error": "No features provided"}), 400

    if not model_loaded:
        return jsonify({"status": "unhealthy", "error": "Model not loaded"}), 500

    prediction = model.predict([features])
    return jsonify({"status": "ok", "prediction": int(prediction[0])}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)