import hashlib
import os
import sqlite3
import string
from tkinter import (
    BooleanVar,
    Button,
    Checkbutton,
    Entry,
    Frame,
    Label,
    StringVar,
    Tk,
)

from pract12 import LoginWindow


class DatabaseHandler:
    def __init__(self) -> None:
        self.conn = sqlite3.connect("users.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
        """)

        self.conn.commit()

    def create_user(self, username: str, pass_hash: str) -> None:
        self.cursor.execute(
            "INSERT OR REPLACE INTO users (username, password_hash) VALUES (?, ?)",
            (username, pass_hash),
        )

        self.conn.commit()

    def get_user(self, username: str):
        self.cursor.execute(
            "SELECT id, username, password_hash FROM users WHERE username = ?",
            (username,),
        )

        user = self.cursor.fetchone()
        return user

    def get_logins(self) -> list[tuple[str, str]]:
        self.cursor.execute("SELECT username, password_hash FROM users")

        return self.cursor.fetchall()

    def clear_users(self) -> None:
        self.cursor.execute("DELETE FROM users")
        self.conn.commit()


class SignUp:
    def __init__(self, db: DatabaseHandler):
        self.db = db

        self.win = Tk()
        self.win.title("Sign Up")
        self.win.geometry("400x200")

        self.main_frame = Frame(self.win)
        self.main_frame.grid(column=0, row=0)

        self.alert_label = Label(self.main_frame, text="")
        self.alert_label.grid(column=0, row=0, columnspan=3)

        self.username = StringVar()
        self.password1 = StringVar()
        self.pass1_entry = Entry(self.main_frame, textvariable=self.password1, show="*")
        self.password2 = StringVar()
        self.pass2_entry = Entry(self.main_frame, textvariable=self.password2, show="*")
        self.show_pass = BooleanVar()

    def create_widgets(self):
        Label(self.main_frame, text="Username").grid(column=0, row=1, columnspan=2)
        Entry(self.main_frame, textvariable=self.username).grid(column=2, row=1)

        Label(self.main_frame, text="Password").grid(column=0, row=2, columnspan=2)
        self.pass1_entry.grid(column=2, row=2)

        Label(self.main_frame, text="Confirm Password").grid(
            column=0, row=3, columnspan=2
        )
        self.pass2_entry.grid(column=2, row=3)

        Checkbutton(
            self.main_frame, variable=self.show_pass, command=self.show_pass_cmd
        ).grid(column=0, row=4)
        Label(self.main_frame, text="Show Password").grid(column=1, row=4)

        Button(self.main_frame, text="Sign Up", command=self.signup).grid(
            column=0, row=5
        )
        Button(self.main_frame, text="Cancel").grid(column=2, row=5)

    def alert(self, text: str, color: str = "red"):
        self.alert_label.config(text=text, fg=color)

    def show_pass_cmd(self):
        if self.show_pass.get():
            self.pass1_entry.config(show="")
            self.pass2_entry.config(show="")
        else:
            self.pass1_entry.config(show="*")
            self.pass2_entry.config(show="*")

    @staticmethod
    def hash_pass(password: str) -> bytes:
        password_bytes = password.encode()
        salt = os.urandom(16)

        key = hashlib.scrypt(password_bytes, salt=salt, n=2**14, r=8, p=1)

        return salt + key

    def verify_signup(self) -> bool:
        username = self.username.get()

        if len(username) < 3:
            self.alert("Username must be at least 3 characters")
            return False

        if self.db.get_user(username) is not None:
            self.alert("User already exists")
            return False

        password = self.password1.get()

        if len(password) < 8:
            self.alert("Password must be at least 8 characters long")
            return False

        if not any(c.isupper() for c in password):
            self.alert("Password must contain at least one uppercase letter")
            return False

        if not any(c.isdigit() for c in password):
            self.alert("Password must contain at least one number")
            return False

        if not any(c in string.punctuation for c in password):
            self.alert("Password must contain at least one special character")
            return False

        if password != self.password2.get():
            self.alert("Passwords do not match")
            return False

        return True

    def signup(self):
        if not self.verify_signup():
            return

        password = self.password1.get()
        pass_hash = self.hash_pass(password)

        self.db.create_user(self.username.get(), pass_hash.hex())
        self.alert("Successfully signed up", color="green")

        self.username.set("")
        self.password1.set("")
        self.password2.set("")

        self.login()

    def login(self):
        login_details = self.db.get_logins()
        app = LoginWindow(self.win, dict(login_details))
        app.create_widgets()

    def run(self):
        self.create_widgets()
        self.win.mainloop()


def main():
    db = DatabaseHandler()
    db.clear_users()
    SignUp(db).run()


main()
