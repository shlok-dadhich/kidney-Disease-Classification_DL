import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

class Prediction:
    def __init__(self,filename):
        self.filename = filename
    
    def predict(self):
        model = load_model("artifacts/training/model.h5")
        img = image.load_img(self.filename,target_size=(224,224))
        img = image.img_to_array(img)
        img = np.expand_dims(img,axis=0)
        result = np.argmax(model.predict(img), axis=1)
        if result[0] == 0:
            prediction = "Cyst"
        elif result[0] == 1:
            prediction = "Normal"
        elif result[0] == 2:
            prediction = "Stone"
        else:
            prediction = "Tumor"
        return prediction
        