from flask import Flask, request
import sqlite3

app = Flask(__name__)

def query(username, password):
    # Mi "connetto" (in questo caso tutto è in memoria) 
    db = sqlite3.connect(':memory:')
    cursor = db.cursor()

    # Confermare le modifiche apportate
    cursor.execute('''CREATE TABLE users (username TEXT, password TEXT)''')
    cursor.execute("INSERT INTO users (username, password) VALUES ('user1', 'password1')")
    cursor.execute("INSERT INTO users (username, password) VALUES ('user2', 'password2')")
    cursor.execute("INSERT INTO users (username, password) VALUES ('user3', 'password3')")
    db.commit() # Confermare le modifiche apportate
    
    # SELECT * FROM users WHERE username='" + username + "' and password='" + password + "'"
    
    cursor.execute("SELECT * FROM users WHERE username='" + username + "' and password='" + password + "'")
    result = cursor.fetchall() # Ricevo il risultato della query
    
    return result

# Sto usando una GET per semplicità, per i login si usa sempre una POST
@app.route('/login', methods=['GET'])
def get_password():
    username = request.args.get('username')
    password = request.args.get('password')

    return query(username, password)
    

if __name__ == '__main__':
    app.run(debug=True)
