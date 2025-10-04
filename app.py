from flask import Flask, request, jsonify,render_template
import os
from flask_cors import CORS,cross_origin
from src.CNNClassifier.pipeline.prediction import Prediction
from src.CNNClassifier.utils.common import read_yaml,decodeImage

os.putenv('LANG','en_US.UTF-8')
os.putenv('LC_ALL','en_US.UTF-8')

app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = "input.jpg"
        self.prediction_pipeline = Prediction(self.filename)    


@app.route("/",methods=['GET'])
@cross_origin()
def home():
    return render_template("index.html")


@app.route("/train",methods=['GET','POST'])
@cross_origin()
def train():
    os.system("python main.py")
    return "Training started!"

@app.route("/predict",methods=['GET','POST'])
@cross_origin()
def predict():
    image = request.json['image']
    client_app = ClientApp()
    decodeImage(image,client_app.filename)
    pred = client_app.prediction_pipeline.predict()
    return jsonify(pred)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)