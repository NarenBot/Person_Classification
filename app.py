from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from utils import decodeImage
from predict import Person

app = Flask(__name__)
CORS(app)


# @cross_origin()
class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = Person(self.filename)


@app.route("/", methods=["GET"])
@cross_origin()
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
@cross_origin()
def predict():
    image = request.json["image"]
    decodeImage(image, clApp.filename)
    result = clApp.classifier.prediction()
    return jsonify(result)


# port = int(os.getenv("PORT"))
if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host="0.0.0.0", port=8080, debug=True)
