from flask import Flask, request, jsonify
from psycopg2 import connect, extras
from cryptography.fernet import Fernet


app = Flask(__name__)
key = Fernet.generate_key()



host = 'localhost'
port = 5433
dbname = 'usersdb'
username = 'postgres'
pasword = 'marioposada'


def get_connection():

    conn = connect(host=host, port=port, dbname=dbname,
                   user=username, password=pasword)
    return conn


@app.get('/api/users')
def get_users():
    return 'Gettings users'


@app.post('/api/users')
def create_user():
    new_user = request.json
    username = new_user['username']
    email = new_user['email']
    password = Fernet(key).encrypt(bytes(new_user['password'], 'utf-8'))
    

    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    cur.execute('INSERT INTO users (username, email, password) VALUES (%s, %s, %s)  RETURNING *',
                (username, email, password))
    new_created_user = cur.fetchone()
    print(new_created_user)
    conn.commit()
    cur.close()
    conn.close()
    

    return jsonify(new_created_user)


@app.delete('/api/users/1')
def delete_user():
    return 'Deleting user'


@app.put('/api/users/1')
def update_user():
    return 'Updating user'


@app.get('/api/users/1')
def get_user():
    return 'Getting user'


if __name__ == '__main__':
    app.run(debug=True)
