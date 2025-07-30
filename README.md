# Project Name
Flask Car Logo Classifier

## Description
This is a web application built with Flask that allows a user to upload a photo of a car logo. Then, a machine learning model analyzes the image and predicts which car manufacturer or model the logo belongs to.

## Main Features
- Simple interface to upload a logo image.
- Automatic logo prediction using a trained model.
- Display of the prediction result on the web page.

## How to Use
1. Run the application with the command:
python app.py

Open your browser and go to:
http://127.0.0.1:5000

Upload a car logo image.

Click “Predict” to see the result.

## Project Structure
app.py: Flask server that handles the upload and prediction.

templates/index.html: Web page to upload images.

static/uploads/: Folder where uploaded images are stored.

ML model file: car_logo_classifier.h5

## Installation
Clone this repository.

Create and activate a virtual environment.

Install dependencies with:
pip install -r requirements.txt
Run the Flask server.

## Author
IKRAMDAOUBIH
