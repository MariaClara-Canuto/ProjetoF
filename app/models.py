import json
import os
import bcrypt
import uuid  

# Caminho para os arquivos JSON
USER_DATA_PATH = os.path.join(os.path.dirname(__file__), 'users.json')
POSTS_DATA_PATH = os.path.join(os.path.dirname(__file__), 'posts.json')

def load_data(file_path, default_value):
    """Carrega dados de um arquivo JSON ou retorna um valor padrão se o arquivo não existir."""
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            json.dump(default_value, file)
    with open(file_path, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return default_value

def save_data(file_path, data):
    """Salva dados em um arquivo JSON."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def load_users():
    """Carrega os usuários do arquivo JSON."""
    return load_data(USER_DATA_PATH, {})

def save_users(users):
    """Salva os usuários no arquivo JSON."""
    save_data(USER_DATA_PATH, users)

def load_posts():
    """Carrega as publicações do arquivo JSON."""
    return load_data(POSTS_DATA_PATH, [])

def save_posts(posts):
    """Salva as publicações no arquivo JSON."""
    save_data(POSTS_DATA_PATH, posts)

def hash_password(password):
    """Gera um hash da senha."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def check_password(hashed_password, user_password):
    """Verifica se a senha do usuário corresponde ao hash."""
    return bcrypt.checkpw(user_password.encode('utf-8'), hashed_password)