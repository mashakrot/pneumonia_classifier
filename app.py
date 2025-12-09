from flask import Flask, request, render_template, flash
import numpy
import tensorflow as tf

print(numpy.__version__)
print(tf.__version__)

from keras.models import load_model
from PIL import Image
from util import classify, image_to_base64
import base64
from io import BytesIO
import os

app = Flask(__name__)

MODEL_PATH = os.path.join("model", "model.h5")
LABELS_PATH = os.path.join("model", "labels.txt")

try:
    model = load_model(MODEL_PATH)
    with open(LABELS_PATH, "r") as f:
        class_names = [line.strip().split(" ")[1] for line in f.readlines()]
except Exception as e:
    raise RuntimeError(f"Error loading model or labels: {e}")


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    img_data = None
    color_class = None

    if request.method == "POST":
        file = request.files.get("file")
        if not file or file.filename == "":
            flash("Please upload a valid image file.", "error")
            return render_template("index.html")

        try:
            image = Image.open(file).convert("RGB")
            class_name, conf_score = classify(image, model, class_names)
            result = f"{class_name} ({conf_score * 100:.1f}%)"

            color_class = "text-red-600" if class_name.lower() == "pneumonia" else "text-green-600"
            img_data = image_to_base64(image)

        except Exception as e:
            flash(f"Error processing image: {e}", "error")

    return render_template("index.html", result=result, img_data=img_data, color_class=color_class)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
