from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Charger le modèle entraîné
model = load_model('car_logo_classifier.h5')  # Remplace par le nom de ton fichier .h5

# Créer un dossier pour stocker les images uploadées
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Liste des noms de classes (à adapter selon ton dataset)
class_names = [
    '1-Volvo', '10-BMW', '11-Jeep', '12-Kia', '13-Citroen',
    '14-Land Rover', '15-Lexus', '16-Mazda', '17-Mercedes',
    '18-Mini', '19-Mitsubishi', '2-Volkswagen', '20-Nissan',
    '21-Opel', '22-Peugeot', '23-Renault', '24-Seat', '25-GMC',
    '26-Smart', '27-Subaru', '28-Suzuki', '29-Tesla', '3-Hyundai',
    '30-Toyota', '31-Alfa Romeo', '32-Acura', '4-Lancia',
    '5-Dacia', '6-Daewoo', '7-Ford', '8-Skoda', '9-Honda'
]


@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    image_path = None

    if request.method == 'POST':
        file = request.files['image']
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            image_path = '/' + file_path  # pour l'affichage dans index.html

            # Traitement de l'image
            img = image.load_img(file_path, target_size=(224, 224))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array /= 255.0  # Normalisation

            # Prédiction
            predictions = model.predict(img_array)
            predicted_class = class_names[np.argmax(predictions)]
            prediction = predicted_class

    # Ici on renvoie le fichier HTML avec les variables
    return render_template("index.html", prediction=prediction, image_path=image_path)

if __name__ == '__main__':
    app.run(debug=True)


