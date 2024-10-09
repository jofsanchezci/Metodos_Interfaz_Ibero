import tkinter as tk
from tkinter import messagebox
import sqlite3

# Configuración de la base de datos
def connect_db():
    conn = sqlite3.connect('crud_tkinter.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Función para insertar un nuevo registro en la base de datos
def add_user():
    name = entry_name.get()
    email = entry_email.get()

    if name and email:
        conn = sqlite3.connect('crud_tkinter.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        conn.close()
        entry_name.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        load_users()
    else:
        messagebox.showwarning("Entrada inválida", "Por favor ingresa tanto el nombre como el email.")

# Función para cargar los registros desde la base de datos a la lista
def load_users():
    for item in listbox_users.get(0, tk.END):
        listbox_users.delete(0, tk.END)

    conn = sqlite3.connect('crud_tkinter.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    for row in cursor.fetchall():
        listbox_users.insert(tk.END, f"{row[0]} - {row[1]} - {row[2]}")
    conn.close()

# Función para eliminar un usuario seleccionado
def delete_user():
    selected = listbox_users.curselection()
    if selected:
        user = listbox_users.get(selected[0])
        user_id = user.split(" - ")[0]

        conn = sqlite3.connect('crud_tkinter.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()
        conn.close()
        load_users()
    else:
        messagebox.showwarning("Selección inválida", "Por favor selecciona un usuario para eliminar.")

# Función para actualizar el usuario seleccionado
def update_user():
    selected = listbox_users.curselection()
    if selected:
        user = listbox_users.get(selected[0])
        user_id = user.split(" - ")[0]
        name = entry_name.get()
        email = entry_email.get()

        if name and email:
            conn = sqlite3.connect('crud_tkinter.db')
            cursor = conn.cursor()
            cursor.execute("UPDATE users SET name = ?, email = ? WHERE id = ?", (name, email, user_id))
            conn.commit()
            conn.close()
            entry_name.delete(0, tk.END)
            entry_email.delete(0, tk.END)
            load_users()
        else:
            messagebox.showwarning("Entrada inválida", "Por favor ingresa tanto el nombre como el email.")
    else:
        messagebox.showwarning("Selección inválida", "Por favor selecciona un usuario para actualizar.")

# Configuración de la ventana principal de Tkinter
root = tk.Tk()
root.title("CRUD con Tkinter y SQLite")

# Widgets de la interfaz de usuario
frame = tk.Frame(root)
frame.pack(pady=10)

label_name = tk.Label(frame, text="Nombre:")
label_name.grid(row=0, column=0, padx=5, pady=5)
entry_name = tk.Entry(frame)
entry_name.grid(row=0, column=1, padx=5, pady=5)

label_email = tk.Label(frame, text="Email:")
label_email.grid(row=1, column=0, padx=5, pady=5)
entry_email = tk.Entry(frame)
entry_email.grid(row=1, column=1, padx=5, pady=5)

button_add = tk.Button(frame, text="Agregar", command=add_user)
button_add.grid(row=2, column=0, padx=5, pady=5)

button_update = tk.Button(frame, text="Actualizar", command=update_user)
button_update.grid(row=2, column=1, padx=5, pady=5)

button_delete = tk.Button(frame, text="Eliminar", command=delete_user)
button_delete.grid(row=2, column=2, padx=5, pady=5)

listbox_users = tk.Listbox(root, width=50)
listbox_users.pack(pady=10)

# Inicializar la base de datos y cargar los usuarios existentes
connect_db()
load_users()

# Ejecutar la aplicación
root.mainloop()
