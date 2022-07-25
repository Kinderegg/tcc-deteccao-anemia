# Importando bibliotecas necessárias
from app import app
from flask import request, render_template, url_for
from keras import models
import numpy as np
from PIL import Image
import string
import random
import os

# Adicionando o caminho para as configurações
app.config['INITIAL_FILE_UPLOADS'] = 'app/static/uploads'

# Carregando o modelo
model = models.load_model('app/static/model/model.h5')

# Roteando para a página inicial
@app.route("/", methods=["GET", "POST"])
def index():

	# Executa se o método de requisição é GET
	if request.method == "GET":
		full_filename =  'images/white_bg.jpg'
		return render_template("index.html", full_filename = full_filename)

	# Executa se o método de requisição é POST
	if request.method == "POST":

		# Gera um nome de imagem único
		letters = string.ascii_lowercase
		name = ''.join(random.choice(letters) for i in range(10)) + '.jpg'
		full_filename =  'uploads/' + name

		# Lê, redimensiona, salva e pré-processa a imagem para predição na CNN 
		image_upload = request.files['image_upload']
		imagename = image_upload.filename
		image = Image.open(image_upload)
		image = image.resize((150,150))
		image.save(os.path.join(app.config['INITIAL_FILE_UPLOADS'], name))
		image_arr = np.array(image.convert('RGB'))
		image_arr.shape = (1,150,150,3)

		# Classificando a imagem
		result = model.predict(image_arr)
		ind = np.argmax(result)
		classes = ['O animal está doente', 'O animal está saudável']

		# Retorna a página, o nome do arquivo e o texto com o resultado
		return render_template('index.html', full_filename = full_filename, pred = classes[ind])

# Função principal
if __name__ == '__main__':
    app.run(debug=True)