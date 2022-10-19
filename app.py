from flask import Flask, request, render_template,redirect
import json
import os
from datetime import date, datetime

app = Flask (__name__)

produtos = []
carrinho = []
relatorio = []

if os.path.exists('produtos.json'): # usa um metodo os, para verificar se o caminho desse arquivo existe
    with open('produtos.json', 'r') as pj: # abre o arquivo em json, cria uma var com os dados do arquivo, e na linha de baixo faz o carregamento dos arquivos.
        produtos = json.load(pj)

def registrar_produtos(produtos): # função de registrar o produto, na linha baixo - utiliza-se a função write para apagar toda a lista e registrar as mudanças.
    with open('produtos.json', 'w') as pj:
        json.dump(produtos, pj)

if os.path.exists('compras.json'): # usa um metodo os, para verificar se o caminho desse arquivo existe
    with open('compras.json', 'r') as cj: # abre o arquivo em json , cria uma var com os dados do arquivo, e na linha de baixo faz o carregamento dos arquivos.
        carrinho = json.load(cj)

def registrar_compras(carrinho): # função de registrar o produto, na linha baixo - utiliza-se a função write para apagar toda a lista e registrar as mudanças.
    with open('compras.json', 'w') as cj:
        json.dump(carrinho, cj)

if os.path.exists('relatorio.json'): # usa um metodo os, para verificar se o caminho desse arquivo existe
    with open('relatorio.json', 'r') as rj: # abre o arquivo em json , cria uma var com os dados do arquivo, e na linha de baixo faz o carregamento dos arquivos.
        relatorio = json.load(rj)

def registrar_relatorio(relatorio): # função de registrar o produto, na linha baixo - utiliza-se a função write para apagar toda a lista e registrar as mudanças.
    with open('relatorio.json', 'w') as rj:
        json.dump(relatorio, rj)

app = Flask(__name__) # criar o programa

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=["POST", "GET"])
def addProduto():
    
    if request.form.get("nomeProduto") and request.form.get("valorProduto"):
        produtos.append({"nomeProduto": request.form.get("nomeProduto"), 'valorProduto': request.form.get('valorProduto')})
        registrar_produtos(produtos)

    return render_template('cadastro.html', produtos = produtos)

@app.route('/<excluirproduto>/removerProduto')
def removerProduto(excluirproduto):
    c = 0
    while c in range (0, len(produtos)):
        if produtos[c]['nomeProduto'] in excluirproduto:
            del produtos[c]
            registrar_produtos(produtos)
            break
        c+=1
    return redirect('/cadastro')

@app.route('/compra')
def compra():
    qtdCompra = len(carrinho)
    c=0
    soma = 0
    
    for c in range (0, len(carrinho)):
        valor = float(carrinho[c]['valorProduto'])
        soma = valor + soma
    

    return render_template('compra.html', produtos = produtos, 
                            carrinho = carrinho, 
                            qtdCompra = qtdCompra,
                            soma = soma)

@app.route('/<nomeProduto>,<valorProduto>/addCompra')
def addCompra(nomeProduto,valorProduto):
    carrinho.append({"nomeProduto": nomeProduto, "valorProduto": valorProduto})
    registrar_compras(carrinho)
    return redirect('/compra')  

@app.route('/<nomeProduto>/rmvCompra')
def rmvCompra(nomeProduto):
    c = 0
    while c in range (0, len(carrinho)):
        if carrinho[c]['nomeProduto'] in nomeProduto:
            del carrinho[c]
            registrar_compras(carrinho)
            break
        c+=1
    registrar_compras(carrinho)
    return redirect('/compra')

@app.route('/finalizar_compra')
def finalizar_compra():
    return render_template('/finalizar_compra.html')

@app.route('/comprafinalizada', methods=["POST", "GET"])
def addRelatorio():

    data = str(date.today())
    soma = 0

    for c in range (0, len(carrinho)):
        valor = float(carrinho[c]['valorProduto'])
        soma = valor + soma
        
    if request.form.get("nomeCliente") and request.form.get("tipopag"):
        relatorio.append({"Data": data, "Valor": valor, 
                        "NomeCliente": request.form.get("nomeCliente"),
                        "TipoPagamento": request.form.get("tipopag"),
                        "Produtos": carrinho })
        registrar_relatorio(relatorio)        
    
    carrinho.clear()
    return redirect('/')

@app.route('/compracancelada')
def rmvRelatorio():
    carrinho.clear()
    return redirect('/relatorio')

@app.route('/relatorio')
def mostrarRelatorio():
    base = relatorio
    return render_template('/mostrarrealatorio.html', base = base)

app.run(debug=True)