from armz_dados import DataRecord
from flask import render_template, redirect, request

class Application:
    def __init__(self):
        self.pages = {
            'pagina': self.pagina,
            'portal': self.portal
        }

        self.__model = DataRecord()
        self.__current_username = None

    def render(self, page, parameter=None):
        content = self.pages.get(page, self.helper)
        if not parameter:
            return content()
        else:
            return content(parameter)

    def get_session_id(self):
        return request.cookies.get('session_id')

    def helper(self):
        return render_template('app/views/html/helper.html')

    def portal(self):
        return render_template('app/views/html/portal.html')

    def pagina(self, username=None):
        if self.is_authenticated(username):
            session_id = self.get_session_id()
            user = self.__model.work_with_parameter(session_id)
            return render_template('app/views/html/pagina.html', current_user=user)
        else:
            return render_template('app/views/html/pagina.html', current_user=None)

    def is_authenticated(self, username):
        session_id = self.get_session_id()
        current_username = self.__model.work_with_parameter(session_id)
        return username == current_username

    def authenticate_user(self, username, password):
        session_id = self.__model.work_with_parameter(username)
        if session_id and session_id.password == password:
            self.logout_user()
            self.__current_username = username
            return session_id.username, username
        return None, None

    def logout_user(self):
        self.__current_username = None
