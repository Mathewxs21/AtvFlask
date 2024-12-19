from flask import Flask, request, render_template, redirect, url_for, flash
from flask_login import LoginManager, logout_user, login_required, login_user
from models import User

app = Flask(__name__)
app.secret_key='marynemateuskaryne'
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.find(id=user_id)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['POST', 'GET'])
def cadastro():
    if request.method == 'POST':
        email = request.form.get('email')
        senha= request.form.get('senha')

        if not email:
            flash('Email é obrigatório')
        else:
            user = User(email=email, senha=senha)
            user.save()
            return redirect(url_for('login'))
    
    return render_template('cadastro.html')


@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        email = request.form['email']
        senha = request.form['senha']
        usuario = User.find(email=email)
    
        if usuario is None:
            return redirect(url_for('cadastro'))
        else:
            login_user(usuario)
            return redirect(url_for('dashboard'))
        
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')
        
@app.route('/logout', methods = ['GET','POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))