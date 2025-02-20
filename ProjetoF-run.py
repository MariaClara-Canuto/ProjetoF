from flask import Flask, request, jsonify, render_template, redirect

app = Flask(__name__, template_folder = 'views/html')

# Rota principal para verificar se o backend está funcionando

@app.route('/', methods=['GET'])
def get_health_route():
    return jsonify({"message": "Backend rodando com sucesso"})

#---------------------------------------------------------------------------------------

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

# Rota login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    elif request.method == 'POST':
        data = request.get_json()  # Obtém os dados JSON enviados pelo frontend
        username = data.get('username')
        password = data.get('password')

        # Verifica se o usuário existe e se a senha está correta
        user = data_record.find_user(username, password)

        if user:
            # Se o usuário for válido, inicia uma sessão
            session['username'] = user.username
            return jsonify({"success": True, "message": "Login bem-sucedido!"})
        else:
            # Se o usuário não for válido, retorna uma mensagem de erro
            return jsonify({"success": False, "message": "Usuário ou senha incorretos"}), 401

#---------------------------------------------------------------------------------------

from app.controllers.controlador import Application # Importação do controlador
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

#---------------------------------------------------------------------------------------

# Iniciar o aplicativo Flask
if __name__ == '__main__':
    app.run(debug=True)