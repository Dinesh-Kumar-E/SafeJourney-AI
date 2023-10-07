import os
import requests


def get_url(model):
    data = {
          "shape_predictor_68_face_landmarks.dat" : r"https://raw.githubusercontent.com/italojs/facial-landmarks-recognition/master/shape_predictor_68_face_landmarks.dat"
     }
    return data[model]

def name(model_name,default = r"resources"):
    model_file_path = os.path.join(default, model_name)
    if (model_name) in os.listdir(default):
        print("Model already exists in : ", model_file_path)
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