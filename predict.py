#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from keras.models import load_model
from keras.preprocessing import image
from keras import utils


class Person:
    def __init__(self, filename):
        self.filename = filename

    def prediction(self):
        # load model
        model = load_model("model.h5")
        # Prediction
        imagename = self.filename
        test_image = utils.load_img(imagename, target_size=(224, 224))
        test_image = utils.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = model.predict(test_image)
        print(result)
        if result[0][0] == 0:
            prediction = "Female"
            return [{"Predicted as ": prediction}]
        else:
            prediction = "Male"
            return [{"Predicted as ": prediction}]
