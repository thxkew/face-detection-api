import cv2
import numpy as np
from flask import Flask, request, jsonify
from face_detection_engine import face_detect

app = Flask(__name__)

@app.route("/detect", methods=['POST'])
def face_detection():
    
    r = request
    nparr = np.fromstring(r.data, np.uint8)
    
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)

    #detect faces
    detected_faces = face_detect(img, cascasdepath='haarcascade_frontalface_default.xml')

    if len(detected_faces) > 0 :
        return jsonify({"detected_faces": detected_faces.tolist()})
    elif len(detected_faces) == 0 :
        return jsonify({"detected_faces": ''})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
