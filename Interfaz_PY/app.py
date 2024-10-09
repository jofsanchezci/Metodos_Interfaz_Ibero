from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Función para conectar a la base de datos
def connect_db():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Ruta principal que muestra los registros
@app.route('/')
def index():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return render_template('index.html', users=users)

# Ruta para agregar un nuevo usuario
@app.route('/add', methods=['POST'])
def add_user():
    name = request.form['name']
    email = request.form['email']
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

# Ruta para editar un usuario existente
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_user(id):
    conn = connect_db()
    cursor = conn.cursor()
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        cursor.execute("UPDATE users SET name = ?, email = ? WHERE id = ?", (name, email, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    else:
        cursor.execute("SELECT * FROM users WHERE id = ?", (id,))
        user = cursor.fetchone()
        conn.close()
        return render_template('edit.html', user=user)

# Ruta para eliminar un usuario
@app.route('/delete/<int:id>')
def delete_user(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Crear la base de datos y la tabla si no existen
    with connect_db() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL
            )
        ''')
    app.run(debug=True)
