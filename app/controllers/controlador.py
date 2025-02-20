from app.controllers.armz_dados import DataRecord
from flask import render_template, redirect, session

class Application:
    def __init__(self):
        self.models = DataRecord()

    def render(self, page, parameter=None):
        if page == 'pagina':
            return self.pagina(parameter)
        if page == 'login':
            return self.login(parameter)
        if page == 'signin':
            return self.signin(parameter)

        else:
            return "Página não encontrada"

    def pagina(self, parameter=None):
        if not parameter:
            return render_template('pagina.html', transfered=False)
        else:
            info = self.models.work_with_parameter(parameter)
            if not info:
                return redirect('/pagina')
            else:
                return render_template('pagina.html', transfered=True, data=info)

    def login(self):
        if request.method == 'POST': 
            data =  request.get_json()
            username = data.get('username')
            password = data.get('password')
            user = self.models.find_user(username, passwaord)

            if user:
                session['username'] = user.username
                return jsonify({'sucsess': True})

            else:
                return jsonify({'success': False, 'message': 'Credênciais Inválidas!'})

        return render_template('login.html')

    def signin(self):
        if request.method == 'POST':
            data = request.get_json()
            username = data.get('username')
            password = data.get('password')

            if self.models.find_user(username, password):
                jsonify({'success': False, 'message': 'Este Usuário já existe.'})

            else:
                jsonify({'success': True})

        return render_template('signin.html')