from tkinter import Button, DoubleVar, Entry, Frame, Label, StringVar, Tk


class TruthTable:
    def __init__(self):
        self.win = Tk()
        self.win.title("Truth Table")
        self.win.geometry("800x600")

        self.main_frame = Frame(self.win)
        self.main_frame.pack(padx=10, pady=10)

        self.temp = DoubleVar(self.win)
        self.result = StringVar(self.win)

    def create_widgets(self):
        pass

    def run(self):
        self.create_widgets()
        self.win.mainloop()


def main():
    TruthTable().run()


main()
