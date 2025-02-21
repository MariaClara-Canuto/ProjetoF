from flask import Flask, render_template, request, redirect, url_for, session, flash
import json
import os

from app import app

# Caminho para o arquivo JSON
USER_DATA_PATH = os.path.join(os.path.dirname(__file__), 'users.json')

def load_users():
    USER_DATA_PATH = os.path.join(os.path.dirname(__file__), 'users.json')
    
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
    USER_DATA_PATH = os.path.join(os.path.dirname(__file__), 'users.json')
    with open(USER_DATA_PATH, 'w') as file:
        json.dump(users, file, indent=4)  # Salva os dados formatados
        
@app.route('/')
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = load_users()
        if username in users:
            flash('Username already exists!')
            return redirect(url_for('register'))
        users[username] = {'password': password}
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
        if username in users and users[username]['password'] == password:
            session['username'] = username
            return redirect(url_for('home'))
        flash('Invalid username or password')
        return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))