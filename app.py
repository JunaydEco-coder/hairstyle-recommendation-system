from flask import Flask, render_template, request
import cv2
from utils.face_shape_predictor import predict_face_shape
from utils.hair_type_classifier import predict_hair_type
from utils.recommender import recommend_hairstyles

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        file = request.files["image"]
        image_path = "demo/upload.jpg"
        file.save(image_path)

        face_shape = predict_face_shape(image_path)
        hair_type = predict_hair_type(image_path)
        recommendations = recommend_hairstyles(face_shape, hair_type)

        result = {
            "face_shape": face_shape,
            "hair_type": hair_type,
            "styles": recommendations
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
