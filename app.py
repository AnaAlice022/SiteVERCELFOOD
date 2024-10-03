from flask import Flask, render_template, redirect, request
import requests

app = Flask(__name__)

url = "https://foodish-api.com/api"

# Lista em memória para armazenar as imagens e descrições
imagens_cadastradas = []


@app.route('/')
def home():
    return render_template('index.html', Titulo='API - Foodish')


@app.route('/cadastro')
def cadastro():
    solicitacao = requests.get(url)
    imagem = solicitacao.json()['image']
    return render_template('cadastro.html', Titulo='API Foodish', imagem=imagem)


@app.route('/galeria')
def galeria():
    return render_template('galeria.html', Titulo='API Foodish', imagensbd=imagens_cadastradas)


@app.route('/criar', methods=['POST'])
def criar():
    imagem = request.form['url']
    descricao = request.form['descricao']

    # Adicionando a imagem e a descrição à lista em memória
    imagens_cadastradas.append((descricao, imagem))

    return redirect('/cadastro')


if __name__ == '__main__':
    app.run(debug=True)
