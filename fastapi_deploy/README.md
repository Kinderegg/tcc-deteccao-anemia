Passos de como rodar essa aplicação:

Passo 1: Faça uma cópia desse projeto.
Passo 2: Abra o prompt de comando e vá para o diretório criado
         onde você encontra o arquivo 'main.py'.
Passo 3: Usando um gerenciador de de implantação de pacotes (aqui usou-se anaconda),
         crie um novo ambiente através do comando:
         conda create -name <environment name>
Passo 4: Ative o ambiente criado usando o comando:
         conda activate <environment name>
Passo 5: Use o comando abaixo para instalar as dependências necessárias:
         python -m pip install -r requirements.txt
Passo 6: Execute a aplicação através do comando:
         uvicorn main:app --reload

Copie e cole a URL informada e cole-a em seu navegador.

Passo 7: Abra a pasta http://127.0.0.1:8000/docs, clique em POST, em seguida no botão Try it out,
         cole o endereço da imagem desejada e execute para obter resultados de classificação. 
Passo 7: Dentro deste projeto existe uma pasta chamada samples onde você
         tem algumas imagens para teste.