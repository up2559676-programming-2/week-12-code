from pract6 import what_to_do_today
from tkinter import Button, DoubleVar, Entry, Frame, Label, StringVar, Tk


class WhatToDoToday:
    def __init__(self):
        self.win = Tk()
        self.win.title("WhatToDoToday")
        self.win.geometry("300x150")

        self.main_frame = Frame(self.win)
        self.main_frame.pack(padx=10, pady=10)

        self.temp = DoubleVar(self.win)
        self.result = StringVar(self.win)

    def create_widgets(self):
        Label(self.main_frame, text="Enter today's tempature").pack()
        Entry(self.main_frame, width=20, textvariable=self.temp).pack()
        Label(self.main_frame, textvariable=self.result).pack()
        Button(
            self.main_frame, text="Reveal today's activity", command=self.activity
        ).pack()

    def activity(self):
        activity = what_to_do_today(self.temp.get())
        self.result.set(f"Today's Activity: {activity}")

    def run(self):
        self.create_widgets()
        self.win.mainloop()


def main():
    WhatToDoToday().run()


main()
