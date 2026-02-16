from tkinter import Tk, Frame, Label, Entry, Button, StringVar, Toplevel
import hashlib
import hmac


class LoginApp:
    def __init__(self, login_details: dict[str, str]) -> None:
        self.root = Tk()
        self.root.withdraw()
        self.window = LoginWindow(self.root, login_details)

    def run(self):
        self.window.create_widgets()
        self.root.mainloop()


class LoginWindow(Toplevel):
    def __init__(self, parent, login_details: dict[str, str]):
        super().__init__(parent)

        self.login_details = login_details
        self.title("Employee Login")
        self.geometry("350x200")

        self.main_frame = Frame(self)
        self.main_frame.grid(column=0, row=0)

        self.username = StringVar()
        self.password = StringVar()
        self.message = StringVar()
        self.message.set("Enter username and password.")

    def create_widgets(self):
        label_message = Label(self.main_frame, textvariable=self.message, width=30)
        label_message.grid(column=0, row=0, columnspan=2)

        label_username = Label(self.main_frame, text="Username:")
        label_username.grid(column=0, row=1)

        entry_username = Entry(self.main_frame, width=25, textvariable=self.username)
        entry_username.grid(column=1, row=1)

        label_password = Label(self.main_frame, text="Password:")
        label_password.grid(column=0, row=2)

        entry_password = Entry(
            self.main_frame, width=25, textvariable=self.password, show="*"
        )
        entry_password.grid(column=1, row=2)

        button_sign_in = Button(
            self.main_frame, text="Sign In", command=self.authenticate
        )
        button_sign_in.grid(column=0, row=3)

        button_cancel = Button(self.main_frame, text="Cancel", command=self.destroy)
        button_cancel.grid(column=1, row=3)

    def authenticate(self):
        username = self.username.get()
        password = self.password.get()

        if username not in self.login_details:
            print("Username not found")
            self.message.set("Username not found.")
            self.main_frame.configure(background="red")
        else:
            stored_value = self.login_details[username]

            is_hashed = len(stored_value) == 128 and all(
                c in "0123456789abcdef" for c in stored_value.lower()
            )

            if not is_hashed:
                if stored_value == password:
                    print("Login successful")
                    self.message.set("Login successful!")
                    self.main_frame.configure(background="green")
                else:
                    print("Incorrect Password")
                    self.message.set("Incorrect password.")
                    self.main_frame.configure(background="yellow")
            else:
                stored_bytes = bytes.fromhex(stored_value)

                if self.verify_pass(password, stored_bytes):
                    print("Login successful")
                    self.message.set("Login successful!")
                    self.main_frame.configure(background="green")
                else:
                    print("Incorrect Password")
                    self.message.set("Incorrect password.")
                    self.main_frame.configure(background="yellow")

    @staticmethod
    def verify_pass(raw_password: str, stored_value: bytes) -> bool:
        salt = stored_value[:16]
        stored_key = stored_value[16:]

        new_key = hashlib.scrypt(raw_password.encode(), salt=salt, n=2**14, r=8, p=1)

        return hmac.compare_digest(new_key, stored_key)


def main():
    company_login_details = {
        "YousefD": "VenterboSS",
        "SergeiT": "25Operyu",
        "YemiO": "Idec704",
        "WinonaS": "IAmMel12",
    }
    app = LoginApp(company_login_details)
    app.run()


if __name__ == "__main__":
    main()
