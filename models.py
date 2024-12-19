from db import get_connection
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha
        self.id = None

    def save(self):
        conn = get_connection()
        conn.execute("INSERT INTO users(email, senha) values(?,?)", (self.email, self.senha))
        conn.commit()
        conn.close()
        return True
    
    @classmethod
    def find(cls, **kwargs):
        conn = get_connection()
        if 'email' in kwargs.keys():
            res = conn.execute("SELECT * from users where email = ?", (kwargs['email'],))
        elif 'id' in kwargs.keys():
            res = conn.execute("SELECT * from users where id = ?", (kwargs['id'],))
        else:
            raise AttributeError('A busca deve ser feita por email ou id.')
        data = res.fetchone()
        if data:
            user = User(email=data['email'], senha=data['senha'])
            user.id = data['id']
            return user
        return None
    
    @classmethod
    def all(cls):
        conn = get_connection()
        users = conn.execute("SELECT * FROM users").fetchall()
        return users