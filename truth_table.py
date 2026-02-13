from tkinter import (
    BooleanVar,
    Button,
    DoubleVar,
    Entry,
    Frame,
    Label,
    StringVar,
    Tk,
)


class TruthTable:
    def __init__(self):
        self.win = Tk()
        self.win.title("Truth Table")
        self.win.geometry("800x600")

        self.main_frame = Frame(self.win)
        self.main_frame.pack(padx=10, pady=10)

        self.temp = DoubleVar(self.win)
        self.result = StringVar(self.win)

        self.answers = [
            BooleanVar(self.win),
            BooleanVar(self.win),
            BooleanVar(self.win),
            BooleanVar(self.win),
        ]

        self.correct_values = [
            False or False,
            False or True,
            True or False,
            True or True,
        ]

    def calculate_score(self):
        score = 0

        for i in range(4):
            try:
                value = self.answers[i].get()  # 0 or 1
                if bool(value) == self.correct_values[i]:
                    score += 1
            except ValueError:
                pass

        percentage = (score / 4) * 100
        self.result.set(f"Score: {percentage:.0f}%")

    def create_widgets(self):
        Label(self.main_frame, text="Truth Table for A OR B").grid(
            row=0, column=0, columnspan=3
        )

        Label(self.main_frame, text="A").grid(row=1, column=0)
        Label(self.main_frame, text="B").grid(row=1, column=1)
        Label(self.main_frame, text="A OR B").grid(
            row=1,
            column=2,
        )

        inputs = [(False, False), (False, True), (True, False), (True, True)]

        for i, (a, b) in enumerate(inputs):
            Label(self.main_frame, text=str(a)).grid(row=i + 2, column=0)
            Label(self.main_frame, text=str(b)).grid(row=i + 2, column=1)

            Entry(self.main_frame, textvariable=self.answers[i], width=10).grid(
                row=i + 2, column=2
            )

        Button(self.main_frame, text="Submit", command=self.calculate_score).grid(
            row=6, column=0, columnspan=3
        )

        Label(self.main_frame, textvariable=self.result).grid(
            row=7, column=0, columnspan=3
        )

    def run(self):
        self.create_widgets()
        self.win.mainloop()


def main():
    TruthTable().run()


main()
