from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
import sqlite3

Window.size = (473, 700)


class database:
    def __init__(self, name):
        self.name = name
        self.connection = sqlite3.connect(self.name)
        self.cursor = self.connection.cursor()

    def close(self):
        self.connection.close()

    def create(self):
        self.cursor.execute("""
        CREATE TABLE if not exists Users(
        id INTEGER primary key,
        username VARCHAR(200),
        email VARCHAR(255) not null unique,
        password VARCHAR(256) not null
        );
        """)
        self.connection.commit()

    def get_all_users(self):
        result = self.cursor.execute("SELECT * from Users;")
        print(result)

    def query_user(self, email, password):
        results = self.cursor.execute(f"SELECT id from Users where email='{email}' and password='{password}'")
        return results.fetchone()


class WelcomeScreen(MDScreen):
    pass


class LoginScreen(MDScreen):
    def try_login(self):
        print("Trying logging")
        input_email = self.ids.email.text
        input_password = self.ids.password.text
        print(input_email, input_password)
        db = database("app_database.db")
        user_id = db.query_user(email=input_email, password=input_password)
        if user_id:
            self.parent.current = "WelcomeScreen"
        else:
            self.ids.login_label.text = "User does not exist"


class RegisterScreen(MDScreen):
    def try_register(self):
        input_user = self.ids.new_user
        input_email = self.ids.new_email.text
        input_password = self.ids.new_password.text



class login(MDApp):
    def build(self):
        return


db = database("app_database.db")
db.create()
db.get_all_users()
m = login()
m.run()
db.close()
