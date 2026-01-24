from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os

from cnnClassifier.utils.common import decodeImage
from cnnClassifier.pipeline.prediction import PredictionPipeline

# -------------------- APP SETUP --------------------
app = Flask(__name__)
CORS(app)

# -------------------- CLIENT APP CLASS --------------------
class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)

# 🔥 IMPORTANT: Create global instance (needed for Gunicorn)
clApp = ClientApp()

# -------------------- ROUTES --------------------

@app.route("/", methods=['GET'])
def home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predictRoute():
    try:
        if not request.json or 'image' not in request.json:
            return jsonify({"error": "No image data provided"}), 400

        image = request.json['image']

        # Decode base64 image to file
        decodeImage(image, clApp.filename)

        # Get prediction
        result = clApp.classifier.predict()

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/train", methods=['GET'])
def trainRoute():
    try:
        os.system("python main.py")
        return "Training completed successfully!"
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# DO NOT use app.run() for Render
# Gunicorn handles the server
