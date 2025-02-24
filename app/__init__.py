from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'simba'

# Inicialize o Socket.IO
socketio = SocketIO(app)

from app import routes  