# Flask App - Sistema de Postagens

## 📌 Descrição
Este é um projeto de um sistema de postagens desenvolvido com **Flask**, onde usuários podem se registrar, fazer login e criar postagens. Apenas usuários com uma **chave especial** podem criar posts. Agora, com **Socket.IO**, todos os usuários podem comentar nas publicações em tempo real.

## 🚀 Funcionalidades
- Cadastro e login de usuários
- Diferenciação entre usuários comuns e especiais
- Apenas usuários especiais podem criar postagens
- Listagem de postagens na página inicial
- Sistema de sessão para autenticação
- **Comentários em tempo real** nas postagens usando **Socket.IO**

## 🛠️ Tecnologias Utilizadas
- **Python 3**
- **Flask**
- **Flask-SocketIO**
- **HTML/CSS/JavaScript**
- **JSON** (para armazenamento de usuários e posts)

## 📂 Estrutura do Projeto
```
Projeto Final/
│-- app/
│   │-- static/
│   │   │-- css/
│   │   │   ├── styles.css
│   │   │-- js/
│   │   │   ├── main.js
│   │-- templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── post.html
│   │   ├── register.html
│   │-- __init__.py
│   │-- models.py
│   │-- routes.py
│   │-- socketio.py
│-- users.json
│-- posts.json
│-- requirements.txt
│-- run.py
│-- venv/
```

## ⚙️ Como Rodar o Projeto
### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2️⃣ Criar e ativar um ambiente virtual (opcional, mas recomendado)
```bash
python3 -m venv venv  # Criar ambiente virtual
source venv/bin/activate  # Ativar no Linux/macOS
venv\Scripts\activate  # Ativar no Windows
```

### 3️⃣ Instalar dependências
```bash
pip install -r requirements.txt
pip install flask-socketio  # Instalar Flask-SocketIO
```

### 4️⃣ Definir variáveis de ambiente
```bash
export FLASK_APP=run.py
export FLASK_ENV=development
flask run
```
No Windows (cmd):
```cmd
set FLASK_APP=run.py
set FLASK_ENV=development
flask run
```

### 5️⃣ Acessar no navegador
Acesse **http://127.0.0.1:5000/** no seu navegador para usar o sistema.

## 🔑 Credenciais Padrão
Você pode modificar os usuários em `users.json`, mas um exemplo de credenciais padrão:

| Usuário  | Senha  | Especial? |
|----------|--------|-----------|
| joao     | 123    | Não       |
| admin    | 456    | Sim       |

## 📜 Licença
Este projeto é de código aberto e pode ser utilizado livremente para estudos e melhorias.

---
Projeto desenvolvido com ❤️ usando **Flask** e **Socket.IO**.

