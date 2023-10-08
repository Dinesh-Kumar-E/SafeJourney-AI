import os
import requests

def get_url(model):
    data = {
        "shape_predictor_68_face_landmarks.dat": r"https://files.catbox.moe/84pk4m.dat"
    }
    return data[model]

def name(model_name, default=r"resources"):
    # Check if the 'default' directory exists, create it if not
    if not os.path.exists(default):
        os.makedirs(default)

    model_file_path = os.path.join(default, model_name)
    if model_name in os.listdir(default):
        print("Model already exists in:", model_file_path)
        return model_file_path
    else:
        print("Downloading model...")
        response = requests.get(get_url(model_name))
        if response.status_code == 200:
            file_name = os.path.join(default, model_name)

            with open(file_name, 'wb') as file:
                file.write(response.content)

            return file_name
        else:
            return None
