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
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('SELECT * FROM users')
    users = cur.fetchall()
    cur.close()
    conn.close()

    return jsonify(users)


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


@app.delete('/api/users/<id>')
def delete_user(id):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    
    cur.execute('DELETE FROM users WHERE id = %s RETURNING *', (id,))
    user = cur.fetchone()
    conn.commit()
    conn.close()
    cur.close()
    
    if user is None:
      return jsonify({'message': 'User not found'}), 404
  
    return  jsonify(user)


  
  


@app.put('/api/users/1')
def update_user():
    return 'Updating user'


@app.get('/api/users/<id>')
def get_user(id):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('SELECT * FROM users WHERE id = %s', (id,))
    user = cur.fetchone()
    if user is None:
        return jsonify({'message': 'User not found'}), 404

    cur.close()
    conn.close()
    return jsonify(user)


if __name__ == '__main__':
    app.run(debug=True)
