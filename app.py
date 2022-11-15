from flask import Flask, request, jsonify
from psycopg2 import connect, extras
from cryptography.fernet import Fernet
from dotenv import load_dotenv
from os import environ


load_dotenv()




app = Flask(__name__)
key = Fernet.generate_key()


host = environ.get('DB_HOST')
port = environ.get('DB_PORT')
dbname = environ.get('DB_NAME')
username = environ.get('DB_USER')
pasword = environ.get('DB_PASSWORD')


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


  
  


@app.put('/api/users/<id>')
def update_user(id):
    
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    update = request.json
    username = update['username']
    email = update['email']
    password = Fernet(key).encrypt(bytes(update['password'], 'utf-8'))
    
    cur.execute('UPDATE users SET username = %s, email = %s, password = %s WHERE id = %s RETURNING *', (username, email, password, id))
    update_user = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    
    if update_user is None:
      return jsonify({'message': 'User not found'}), 404
  
    return jsonify(update_user)


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
