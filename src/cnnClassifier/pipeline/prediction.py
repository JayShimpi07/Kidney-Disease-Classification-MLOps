import numpy as np
from tensorflow import keras
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

class PredictionPipeline:
    def __init__(self,filename):
        self.filename =filename

    def predict(self):
        # load model
        model = load_model(os.path.join("model", "model.h5"))
        imagename = self.filename
        test_image = image.load_img(imagename, target_size=(224, 224))
        test_image = image.img_to_array(test_image) / 255.0   # ✅ normalize
        test_image = np.expand_dims(test_image, axis=0)

        # prediction
        probs = model.predict(test_image)[0]   # example: [0.90, 0.10]
        pred_index = int(np.argmax(probs))
        confidence = float(np.max(probs)) * 100

        # label mapping
        if pred_index == 1:
            prediction = "Tumor"
        else:
            prediction = "Normal"

        return [
    {
        "prediction": prediction,
        "confidence": round(confidence, 2),
        "probabilities": {
            "Normal": round(float(probs[0]) * 100, 2),
            "Tumor": round(float(probs[1]) * 100, 2)
        }
    },
    {
        "image": ""   # placeholder so frontend doesn't crash
    }
]

