from flask import Flask, render_template, request, redirect
from flask import url_for
import pandas as pd
import numpy as np


app = Flask(__name__)

produtos = []
carrinho = []


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/produto_cadastrado')
def cadastrado_ok():
    argumentos = request.args.to_dict()
    produtos.append(argumentos)
    return render_template('produto_cadastrado.html', lista=produtos)


@app.route('/listar_cadastrados')
def listagen():
    #return produtos
    return render_template('listar.html', lista=produtos)



@app.route('/vendas')
def vendas():
    return render_template('adc_carrinho.html', lista=produtos)

@app.route('/carrinho_cad')
def cadastrado_carrinho():
    prod_vendido = request.args.to_dict()
    carrinho.append(prod_vendido)
    return render_template('carrinho_cad.html', carrinho=carrinho)

@app.route('/carrinho')
def adc_carrinho():
    return render_template('listar_carrinho.html', carrinho=carrinho)




if __name__ == "__main__":
    app.run(debug=True)