
from flask import Flask, request, render_template
import json
import os


app = Flask (__name__)

produtos = []

if os.path.exists('produtos.json'): # usa um metodo os, para verificar se o caminho desse arquivo existe
    with open('produtos.json', 'r') as pj: # abre o arquivo em json, cria uma var com os dados do arquivo, e na linha de baixo faz o carregamento dos arquivos.
        produtos = json.load(pj)

def registrar_produtos(produtos): # função de registrar o produto, na linha baixo - utiliza-se a função write para apagar toda a lista e registrar as mudanças.
    with open('produtos.json', 'w') as pj:
        json.dump(produtos, pj)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=["POST", "GET"])
def addProduto():
    if request.form.get("nomeProduto") and request.form.get("valorProduto"):
        produtos.append({"nomeProduto": request.form.get("nomeProduto"), 'valorProduto': request.form.get('valorProduto')})
        registrar_produtos(produtos)
    return render_template('cadastro.html', produtos = produtos)

app.run(debug=True)