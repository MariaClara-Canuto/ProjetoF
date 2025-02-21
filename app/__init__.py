from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'simba'

from app import routes  # Certifique-se de que as rotas estão sendo importadas
