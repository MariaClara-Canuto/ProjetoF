from flask import Flask, render_template, request, redirect, url_for, session, flash
import json
import os
import bcrypt

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Caminho para o arquivo JSON de usuários
USER_DATA_PATH = os.path.join(os.path.dirname(__file__), 'users.json')

# Caminho para o arquivo JSON de publicações
POSTS_DATA_PATH = os.path.join(os.path.dirname(__file__), 'posts.json')

def load_users():
    # Se o arquivo não existir, cria um arquivo com um objeto JSON vazio
    if not os.path.exists(USER_DATA_PATH):
        with open(USER_DATA_PATH, 'w') as file:
            json.dump({}, file)  # Inicializa com um objeto vazio
    
    # Abre o arquivo e carrega os dados
    with open(USER_DATA_PATH, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            # Se o arquivo estiver vazio ou malformado, retorna um objeto vazio
            return {}

def save_users(users):
    with open(USER_DATA_PATH, 'w') as file:
        json.dump(users, file, indent=4)  # Salva os dados formatados

def load_posts():
    # Se o arquivo não existir, cria um arquivo com uma lista vazia
    if not os.path.exists(POSTS_DATA_PATH):
        with open(POSTS_DATA_PATH, 'w') as file:
            json.dump([], file)  # Inicializa com uma lista vazia
    
    # Abre o arquivo e carrega os dados
    with open(POSTS_DATA_PATH, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_posts(posts):
    with open(POSTS_DATA_PATH, 'w') as file:
        json.dump(posts, file, indent=4)  # Salva os dados formatados

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def check_password(hashed_password, user_password):
    return bcrypt.checkpw(user_password.encode('utf-8'), hashed_password)

@app.route('/')
def home():
    if 'username' in session:
        users = load_users()
        username = session['username']
        posts = load_posts()  # Carrega as publicações
        return render_template('home.html', username=username, users=users, posts=posts)
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        special_key = request.form.get('special_key', '')  # Obtém a chave especial (se existir)
        
        users = load_users()
        
        if username in users:
            flash('Username already exists!')
            return redirect(url_for('register'))
        
        # Verifica se a chave especial está correta
        SPECIAL_KEY = "minha_chave_secreta"  # Defina sua chave especial aqui
        is_special = (special_key == SPECIAL_KEY)
        
        # Cria o usuário
        hashed_password = hash_password(password)
        users[username] = {
            'password': hashed_password.decode('utf-8'),
            'is_special': is_special  # Marca se o usuário é especial
        }
        
        save_users(users)
        flash('Registration successful! Please login.')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = load_users()
        if username in users and check_password(users[username]['password'].encode('utf-8'), password):
            session['username'] = username
            return redirect(url_for('home'))
        flash('Invalid username or password')
        return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/post', methods=['GET', 'POST'])
def post():
    if 'username' not in session:
        flash('You need to login first!')
        return redirect(url_for('login'))
    
    users = load_users()
    username = session['username']
    
    # Verifica se o usuário é especial
    if not users.get(username, {}).get('is_special', False):
        flash('You do not have permission to post!')
        return redirect(url_for('home'))
    
    if request.method == 'POST':
        post_content = request.form['post_content']
        
        # Carrega as publicações existentes
        posts = load_posts()
        
        # Adiciona a nova publicação
        posts.append({
            'username': username,
            'content': post_content
        })
        
        # Salva as publicações atualizadas
        save_posts(posts)
        
        flash('Post published successfully!')
        return redirect(url_for('post'))
    
    return render_template('post.html')