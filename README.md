# Person_Classification
This Repo is for whether the model classifies the person as Male or Female in computer vision technique.

# Models Used:
Tensorflow

# Packages and Tools used:
OpenCV, Pillow, Flask, Flask-Cors, VScode, Docker

# How to work:
### Steps to follow:
```bash
- conda create -n <envname> python==3.8 -y
- git clone https://github.com/NarenBot/Person_Classification.git
- pip install -r requirements.txt
- python app.py
```
- Upload any male or female image and click predict button, thats it.
- Use test_images inside Images folder for Prediction or you can use the outside file.
    - Note: The given test_images are not used in training process.

# Process of code:
- Initialize ClientApp class with filename as 'inputImage.jpg'
- When we uploaded the image, it will encode into base64 using javascript.
- Once you click the predict button, the user request the encoded image and decode it.
- After decoding the image, an 'inputImage.jpg' file was created.
- Then it will passes through the prediction function in Person class.
- Here the image will converted to array, expand the dimensions and finally predicted in JSON format.

