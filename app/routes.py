import os
import uuid
from flask_socketio import emit
from flask import Flask, render_template, request, redirect, url_for, session, flash
from app import app, socketio
from app.models import load_users, save_users, load_posts, save_posts, hash_password, check_password

#função para garantir que todas as publicações tenham um ID
def garantir_ids_nos_posts():
    posts = load_posts()
    for post in posts:
        if 'id' not in post:
            post['id'] = str(uuid.uuid4())  # Adiciona um ID único se não existir
    save_posts(posts)

# Chame essa função ao iniciar o aplicativo
garantir_ids_nos_posts()

@app.route('/')
def home():
    if 'username' in session:
        users = load_users()
        username = session['username']
        posts = load_posts()
        return render_template('home.html', username=username, users=users, posts=posts)
    return redirect(url_for('login'))

# Rota para enviar comentários via Socket.IO
@socketio.on('comentar')
def handle_comentario(data):
    username = session.get('username')
    if not username:
        return
    
    post_id = data['post_id']
    comentario = data['comentario']
    
    # Carregue as publicações
    posts = load_posts()
    
    # Encontre a publicação correspondente
    post_encontrado = None
    for post in posts:
        if post.get('id') == post_id:  # Use .get() para evitar KeyError
            post_encontrado = post
            break
    
    if not post_encontrado:
        print(f"Publicação com ID {post_id} não encontrada.")
        return
    
    # Adicione o comentário à publicação correspondente
    if 'comentarios' not in post_encontrado:
        post_encontrado['comentarios'] = []
    post_encontrado['comentarios'].append({
        'username': username,
        'comentario': comentario
    })
    
    # Salve as publicações atualizadas
    save_posts(posts)
    
    # Emita o comentário para todos os clientes
    emit('novo_comentario', {
        'post_id': post_id,
        'username': username,
        'comentario': comentario
    }, broadcast=True)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        special_key = request.form.get('special_key', '')
        
        users = load_users()
        
        if username in users:
            flash('Username already exists!')
            return redirect(url_for('register'))
        
        SPECIAL_KEY = "simba"
        is_special = (special_key == SPECIAL_KEY)
        
        hashed_password = hash_password(password)
        users[username] = {
            'password': hashed_password.decode('utf-8'),
            'is_special': is_special
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

@app.route('/logout', methods=['POST'])
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
    
    if not users.get(username, {}).get('is_special', False):
        flash('You do not have permission to post!')
        return redirect(url_for('home'))
    
    if request.method == 'POST':
        post_content = request.form['post_content']
        
        posts = load_posts()
        posts.append({
            'id': str(uuid.uuid4()),
            'username': username,
            'content': post_content,
            'comentarios': []
        })
        save_posts(posts)
        
        flash('Post published successfully!')
        return redirect(url_for('post'))
    
    return render_template('post.html')