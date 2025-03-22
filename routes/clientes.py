from flask import Blueprint, render_template

cliente_route = Blueprint('cliente', __name__)

@cliente_route.route('/')
def lista_clientes():
    pass


@cliente_route.route('/<int:cliente_id>')
def obter_cliente(cliente_id):
    pass