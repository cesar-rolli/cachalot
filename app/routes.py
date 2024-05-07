from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    # Obtendo o endereço IP do cliente
    client_ip = request.remote_addr
    return f'O seu endereço IP é: {client_ip}'

if __name__ == '__main__':
    app.run()
