from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import get_file 
from tensorflow.keras.utils import load_img 
from tensorflow.keras.utils import img_to_array
from tensorflow import expand_dims
from tensorflow.nn import softmax
from numpy import argmax
from numpy import max
from numpy import array
from json import dumps
from uvicorn import run
import os
from PIL import Image

app = FastAPI()

origins = ["*"]
methods = ["*"]
headers = ["*"]

app.add_middleware(
    CORSMiddleware, 
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = methods,
    allow_headers = headers    
)

model_dir = "model.h5"
model = load_model(model_dir)

class_predictions = array([
    'saudavel',
    'doente',
])

@app.get("/")
async def root():
    return {"mensagem": "Bem-vindo à API de detecção de anemia em ovinos da UFC!"}

@app.post("/net/image/prediction/")
async def get_net_image_prediction(image_link: str = ""):
    if image_link == "":
        return {"mensagem": "Não foi fornecido link para nenhuma imagem."}
    
    #abre a imagem
    image_upload = image_link
    img_path = Image.open(image_upload)
    
    #trata a imagem
    img_path = img_path.resize((150,150))
    img_path = array(img_path.convert('RGB'))
    img_path.shape = (1,150,150,3)
    
    #faz a previsao
    pred = model.predict(img_path)
    score = pred[0]

    #armazena índice de probabilidade mais alta
    class_prediction = class_predictions[argmax(score)]

    return {
        "previsao": class_prediction,
    }

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    run(app, host="0.0.0.0", port=port)