from armz_dados import DataRecord
from flask import render_template, redirect

class Application:
    def __init__(self):
        self.models = DataRecord()

    def render(self, page, parameter=None):
        if page == 'pagina':
            return self.pagina(parameter)
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