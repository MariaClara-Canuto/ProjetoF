from flask import Flask, request, jsonify, render_template, redirect

app = Flask(__name__)

# Rota principal para verificar se o backend está funcionando
@app.route('/', methods=['GET'])
def get_health_route():
    return jsonify({"message": "Backend rodando com sucesso"})

# Rota GET simples
@app.route('/get', methods=['GET'])
def get_route():
    return jsonify({"message": "Rota GET acessada com sucesso"})

# Rota POST para receber dados JSON
@app.route('/post', methods=['POST'])
def post_route():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Nenhum dado recebido"}), 400
    return jsonify({"received_data": data})

# Rota DELETE
@app.route('/delete', methods=['DELETE'])
def delete_route():
    return jsonify({"message": "Objeto deletado com sucesso"}), 200

# Importação do controlador
from controlador import Application

# Instanciando o controlador
application = Application()

# Rota para renderizar uma página sem parâmetro
@app.route('/pagina', methods=['GET'])
def pagina_route():
    return application.render('pagina')

# Rota para renderizar uma página com parâmetro
@app.route('/pagina/<parameter>', methods=['GET'])
def pagina_with_parameter_route(parameter):
    return application.render('pagina', parameter)

# Iniciar o aplicativo Flask
if __name__ == '__main__':
    app.run(debug=True)