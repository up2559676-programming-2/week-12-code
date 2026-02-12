from tkinter import Button, DoubleVar, Entry, Frame, Label, StringVar, Tk

from pract5 import area_of_circle, circumference_of_circle


class CircleInfo:
    def __init__(self):
        self.win = Tk()
        self.win.title("Calculator")
        self.win.geometry("250x250")

        self.main_frame = Frame(self.win)
        self.main_frame.pack(padx=10, pady=10)

        self.radius = DoubleVar(self.win)

        self.area_text = StringVar(self.win, value="Area: 0 cm²")
        self.circ_text = StringVar(self.win, value="Circumference: 0 cm")

    def create_widgets(self):
        Label(self.main_frame, text="Radius in cm:").pack()
        Entry(self.main_frame, textvariable=self.radius).pack()

        Label(self.main_frame, textvariable=self.area_text).pack()
        Label(self.main_frame, textvariable=self.circ_text).pack()

        Button(self.main_frame, text="Calculate", command=self.calculate).pack(
            side="left"
        )
        Button(self.main_frame, text="Close", command=self.win.destroy).pack(
            side="right"
        )

    def calculate(self):
        area = area_of_circle(self.radius.get())
        circ = circumference_of_circle(self.radius.get())

        self.area_text.set(f"Area: {area:.2f} cm²")
        self.circ_text.set(f"Circumference: {circ:.2f} cm")

    def run(self):
        self.create_widgets()
        self.win.mainloop()


def main():
    CircleInfo().run()


main()
