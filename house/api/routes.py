from flask import Blueprint

mod = Blueprint('api', __name__)

@mod.route('/obtener')
def obtener():
	return '{"result" : "You are in the API!!!"}'
