from flask import render_template
from application import app
from application.model.dao.item_dao import Item_DAO,Item

@app.route("/", methods=['GET'])
def home():
    itens_lista = Item_DAO().estoqueBuscape()
    return render_template("home.html", itens_lista = itens_lista,)

@app.route("/carrinho",methods=['GET'])
def carrinho():
    return render_template('carrinho.html', )