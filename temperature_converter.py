from tkinter import Button, DoubleVar, Entry, Frame, Label, Tk


class TemperatureConverter:
    def __init__(self):
        self.win = Tk()
        self.win.title("Temperature Converter")
        self.win.geometry("350x100")

        self.main_frame = Frame(self.win)
        self.main_frame.grid(column=0, row=0)

        self.celsius = DoubleVar(self.win)
        self.fahrenheit = DoubleVar(self.win)

    def create_widgets(self):
        Label(self.main_frame, text="Celsius").grid(row=0, column=0)
        Entry(self.main_frame, textvariable=self.celsius).grid(row=1, column=0)
        Button(
            self.main_frame, text="Convert to Fahrenheit", command=self.convert_celsius
        ).grid(row=2, column=0)

        Label(self.main_frame, text="Fahrenheit").grid(row=0, column=1)
        Entry(self.main_frame, textvariable=self.fahrenheit).grid(row=1, column=1)
        Button(
            self.main_frame, text="Convert to Celsius", command=self.convert_fahrenheit
        ).grid(row=2, column=1)

    def convert_celsius(self):
        cels = self.celsius.get()
        self.fahrenheit.set(cels * 9 / 5 + 32)

    def convert_fahrenheit(self):
        fahr = self.fahrenheit.get()
        self.celsius.set((fahr - 32) / (9 / 5))

    def run(self):
        self.create_widgets()
        self.win.mainloop()


def main():
    TemperatureConverter().run()


main()
