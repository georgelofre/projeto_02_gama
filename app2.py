from flask import Flask, request, render_template,redirect

products = []
app = Flask (__name__)
@app.route('/')
def index():
    return render_template('001_index.html')
    
@app.route('/fornecedor')
def fornecedor():
    return render_template('001_portal_fornecedor.html')

@app.route('/consumidor')
def consumidor():
    return render_template('001_portal_consumidor.html')

@app.route('/relatorio')
def relatorio():
    return render_template('001_relatorio.html')

@app.route('/fornecedor/cadastrar', methods=['POST', 'GET'])
def cadastrar():
    if request.method == 'GET':
        return render_template('001_cadastrar_produto.html')
    elif request.method == 'POST':
        nome = request.form['nome']
        preco = request.form['preco']
        products.append({"nome":nome, "preco":preco})
        return redirect ('/fornecedor/cadastrar')

@app.route('/fornecedor/listarcad')
def listarcad():
    return render_template('001_listar_produtos_cadastrados.html')

@app.route('/fornecedor/excluircad')
def excluircad():
    return render_template('001_excluir_cadastro.html')

@app.route('/consumidor/adicionar')
def adicionar():
    return render_template('001_adicionar_no_carrinho.html')

@app.route('/consumidor/visualizar')
def visualizar():
    return render_template('001_listar_produtos_carrinho.html')

@app.route('/consumidor/excluir')
def excluir():
    return render_template('001_excluir_carrinho.html')

@app.route('/consumidor/finalizar')
def finalizar():
    return render_template('001_compra_finalizada.html')



app.run(debug=True)