from flask import render_template, request
from application import app
from application.model.dao.item_dao import Item_DAO, carrinhoCompras

@app.route("/", methods=['GET'])
def home():
    itens_lista = Item_DAO().estoqueBuscape()
    print(carrinhoCompras)
    return render_template("home.html", carrinhoCompras = carrinhoCompras , itens_lista = itens_lista,)

@app.route("/carrinho",methods=['GET'])
def carrinho():
    return render_template('home.html', carrinhoCompras = carrinhoCompras )

@app.route("/adicionar", methods=['POST'])
def inserir():
    itens_lista = Item_DAO().estoqueBuscape()
    id = request.form.get('id', None)
    print(id)
    for iten in itens_lista:
        if iten.id == id:
            carrinhoCompras.append(iten)
        else:
            continue
    
    return render_template('home.html', carrinhoCompras = carrinhoCompras)
        
@app.route("/remover/<int:id>", methods=['GET'])
def remover(id:int):
    for iten in carrinhoCompras:
        if iten.id == '{}'.format(id):
            carrinhoCompras.remove(iten)
            return render_template("home.html", carrinhoCompras = carrinhoCompras)
    return render_template("home.html", carrinhoCompras = carrinhoCompras),404
    