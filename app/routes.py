from app import app
from flask import jsonify
from flask import request
import jsonpickle

@app.route('/', methods=["GET"])

def index():
  ip_addr = request.remote_addr                  # IP do usuario
  navegador = request.headers.get('User-Agent')  # plataforma, navegador, versão, língua, 
  return navegador + '---------' + ip_addr