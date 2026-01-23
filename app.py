from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from cnnClassifier.utils.common import decodeImage
from cnnClassifier.pipeline.prediction import PredictionPipeline

os.putenv("LANG", "en_US.UTF-8")
os.putenv("LC_ALL", "en_US.UTF-8")

app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)


@app.route("/", methods=["GET"])
@cross_origin()
def home():
    return render_template("index.html")


@app.route("/train", methods=["GET", "POST"])
@cross_origin()
def trainRoute():
    os.system("python main.py")
    # os.system("dvc repro")
    return "✅ Training done successfully!"


@app.route("/predict", methods=["POST"])
@cross_origin()
def predictRoute():
    try:
        data = request.get_json(force=True)

        if data is None or "image" not in data:
            return jsonify({"error": "No image found in request body"}), 400

        image_b64 = data["image"]

        # ✅ handle base64 header if present
        if "," in image_b64:
            image_b64 = image_b64.split(",")[1]

        # ✅ decode and save
        decodeImage(image_b64, clApp.filename)

        # ✅ predict
        result = clApp.classifier.predict()

        return jsonify(result)

    except Exception as e:
        # ✅ return actual error to frontend (helps debugging)
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    clApp = ClientApp()

    # ✅ Debug=True for development (shows errors clearly)
    # Set debug=False when deploying
    app.run(host="0.0.0.0", port=8080, debug=True)
