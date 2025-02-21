from flask import Flask, request, jsonify, render_template, redirect, Response
from controlador import Application

app = Flask(__name__)
application = Application()

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

# Rota para renderizar uma página sem parâmetro
@app.route('/pagina', methods=['GET'])
def pagina_route():
    return application.render('pagina')

# Rota para renderizar uma página com parâmetro
@app.route('/pagina/<parameter>', methods=['GET'])
def pagina_with_parameter_route(parameter):
    return application.render('pagina', parameter)

#@app.route('/portal', methods=['POST'])
#def action_portal():
#    username = request.form.get('username')
#    password = request.form.get('password')
#
#    print(f"usuário recebido{username}, Senha recebida: {password}")
    
#    session_id, username = application.authenticate_user(username, password)

#    if session_id:
#        resp = Response()
#        resp.set_cookie('session_id', session_id, httponly=True, secure=True, max_age=3600)
#        return redirect(f'/pagina/{username}')
    
#    else:
#        return redirect('/portal')

@app.route('/portal', methods=['POST'])
def action_portal():
    print("Recebendo requisição POST em /portal")  # Log para depuração

    username = request.form.get('username')
    password = request.form.get('password')

    print(f"Usuário recebido: {username}, Senha recebida: {password}")  # Mostra os valores no terminal

    if not username or not password:
        return jsonify({"error": "Usuário ou senha não fornecidos"}), 400

    session_id, username = application.authenticate_user(username, password)

    if session_id:
        response = make_response(redirect(f'/pagina/{username}'))  # Correção aqui!
        response.set_cookie('session_id', session_id, httponly=True, secure=True, max_age=3600)
        return response  # Agora retorna a resposta corretamente!
    else:
        return jsonify({"error": "Credenciais inválidas"}), 401

@app.route('/logout', methods=['POST'])
def logout():
    application.logout_user()
    resp = Response()
    resp.delete_cookie('session_id')
    return redirect('/helper')

# Iniciar o aplicativo Flask
if __name__ == '__main__':
    app.run(debug=True)
