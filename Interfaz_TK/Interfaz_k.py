import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.recycleview import RecycleView
import sqlite3

kivy.require('1.11.1')


class UserRecycleView(RecycleView):
    def __init__(self, **kwargs):
        super(UserRecycleView, self).__init__(**kwargs)
        self.data = []

class CRUDApp(BoxLayout):
    def __init__(self, **kwargs):
        super(CRUDApp, self).__init__(**kwargs)
        self.orientation = 'vertical'

        # Configuración de la base de datos SQLite
        self.conn = sqlite3.connect('crud_kivy.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL
            )
        ''')
        self.conn.commit()

        # Crear interfaz gráfica
        self.name_input = TextInput(hint_text='Nombre', multiline=False)
        self.email_input = TextInput(hint_text='Email', multiline=False)
        self.add_widget(self.name_input)
        self.add_widget(self.email_input)

        self.button_layout = BoxLayout(size_hint_y=None, height=50)
        self.add_button = Button(text='Agregar', on_press=self.add_user)
        self.update_button = Button(text='Actualizar', on_press=self.update_user)
        self.delete_button = Button(text='Eliminar', on_press=self.delete_user)
        self.button_layout.add_widget(self.add_button)
        self.button_layout.add_widget(self.update_button)
        self.button_layout.add_widget(self.delete_button)
        self.add_widget(self.button_layout)

        self.user_list = UserRecycleView()
        self.add_widget(self.user_list)
        self.load_users()

    def load_users(self):
        self.user_list.data = []
        self.cursor.execute("SELECT * FROM users")
        for user in self.cursor.fetchall():
            self.user_list.data.append({'text': f"{user[0]} - {user[1]} - {user[2]}"})

    def add_user(self, instance):
        name = self.name_input.text
        email = self.email_input.text
        if name and email:
            self.cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
            self.conn.commit()
            self.name_input.text = ''
            self.email_input.text = ''
            self.load_users()

    def update_user(self, instance):
        selected_user = self.user_list.data[0]['text'].split(' - ')[0]
        name = self.name_input.text
        email = self.email_input.text
        if selected_user and name and email:
            self.cursor.execute("UPDATE users SET name = ?, email = ? WHERE id = ?", (name, email, selected_user))
            self.conn.commit()
            self.name_input.text = ''
            self.email_input.text = ''
            self.load_users()

    def delete_user(self, instance):
        selected_user = self.user_list.data[0]['text'].split(' - ')[0]
        if selected_user:
            self.cursor.execute("DELETE FROM users WHERE id = ?", (selected_user,))
            self.conn.commit()
            self.load_users()

    def on_stop(self):
        self.conn.close()


class CRUDKivyApp(App):
    def build(self):
        return CRUDApp()


if __name__ == '__main__':
    CRUDKivyApp().run()
