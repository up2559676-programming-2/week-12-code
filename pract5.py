import math

from graphix import Window, Circle, Point, Line, Text


def greet(name: str) -> str:
    return f"Hello, {name}!"


def product(a: float, b: float):
    return a * b


def divide(a: float, b: float):
    return a / b


def divide_and_product(a: float, b: float) -> tuple[float, float]:
    product_result = product(a, b)
    divide_result = divide(a, b)
    return product_result, divide_result


def main():
    my_name = input("What is your name? ")
    greeting = greet(my_name)
    print(greeting)

    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    product_result, divide_result = divide_and_product(num1, num2)
    print(f"{num1} * {num2} = {product_result}")
    print(f"{num1} / {num2} = {divide_result}")


def calc_future_value(amount: float, years: int) -> float:
    interest_rate = 0.065
    for _ in range(years):
        amount = amount * (1 + interest_rate)
    return amount


def future_value():
    amount = float(input("Enter an amount to invest: "))
    years = int(input("Enter the number of years: "))
    final = calc_future_value(amount, years)

    output = f"Investing £{amount:0.2f} for {years} years "
    output += f"results in £{final:0.2f}."
    print(output)


# For exercises 1 and 2


def area_of_circle(radius: float) -> float:
    return math.pi * radius**2


# For exercise 3
def draw_circle(win: Window, centre: Point, radius: int, colour: str):
    circle = Circle(centre, radius)
    circle.fill_colour = colour
    circle.outline_width = 2
    circle.draw(win)


def draw_brown_eye_in_centre():
    window = Window()

    for rad in (120, 60, 30):
        draw_circle(window, Point(window.width // 2, window.height // 2), rad, "brown")

    window.get_mouse()


# For exercise 5
def draw_brown_eye(win: Window, centre: Point, radius: int):
    eye_radius = [radius, radius // 2, radius // 4]
    eye_colours = ["white", "brown", "black"]

    for radius, colour in zip(eye_radius, eye_colours):
        draw_circle(win, centre, radius, colour)


def circumference_of_circle(radius: float) -> float:
    return math.pi * radius * 2


def circle_info():
    radius = float(input("Enter radius of the circle: "))

    area = area_of_circle(radius)
    circumference = circumference_of_circle(radius)

    print(f"The area is {area:.3f} and the circumference is {circumference:.3f}")


def draw_block_of_stars(width: int, height: int):
    char = "*"
    line = char * width + "\n"
    print(line * height, end="")


def draw_letter_e():
    component_height = 2
    components = (8, 2, 5, 2, 8)

    for c in components:
        draw_block_of_stars(c, component_height)


def draw_pair_of_brown_eyes():
    win = Window(width=600, height=400)
    radius = 120
    win_centre = (win.width // 2, win.height // 2)

    draw_brown_eye(win, Point(win_centre[0] - radius, win_centre[1]), radius)
    draw_brown_eye(win, Point(win_centre[0] + radius, win_centre[1]), radius)

    win.get_mouse()


def distance_between_points(p1: Point, p2: Point) -> float:
    a = p2.x - p1.x
    b = p2.y - p1.y

    return math.sqrt(a**2 + b**2)


def distance_calculator():
    win = Window()

    p1 = win.get_mouse()
    p2 = win.get_mouse()

    Line(p1, p2).draw(win)
    Text(Point(win.width // 2, 20), str(distance_between_points(p1, p2))).draw(win)

    win.get_mouse()


def draw_blocks(
    height: int, space1: int = 0, width1: int = 0, space2: int = 0, width2: int = 0
):
    space = " "
    char = "*"

    line = space * space1 + char * width1 + space * space2 + char * width2 + "\n"
    print(line * height, end="")


def draw_letter_a():
    draw_blocks(2, 1, 8, 1)
    draw_blocks(2, 0, 2, 6, 2)
    draw_blocks(2, 0, 10)
    draw_blocks(2, 0, 2, 6, 2)


def draw_four_pairs_of_brown_eyes():
    pass


def display_text_with_spaces(win: Window, text: str, pos: Point, size: int):
    text = "".join(char + " " for char in text.upper())
    text_display = Text(pos, text)
    text_display.size = size
    text_display.draw(win)


def construct_vision_chart():
    strings = [input(f"Enter string {i + 1}") for i in range(6)]
    string_sizes = [30, 25, 20, 15, 10, 5]
    spacing = 50

    win = Window()
    for i, (string, size) in enumerate(zip(strings, string_sizes)):
        display_text_with_spaces(
            win, string, Point(win.width // 2, size + spacing * i), size
        )

    win.get_mouse()


def draw_stick_figure(win: Window, size: int, pos: Point):
    head = Circle(pos, size)
    head.draw(win)

    body_y_start = pos.y + size
    body_y_end = pos.y + size * 3
    body = Line(Point(pos.x, body_y_start), Point(pos.x, body_y_end))
    body.draw(win)

    arms_y = body_y_start + size // 2
    arms = Line(
        Point(pos.x - int(size * 1.5), arms_y), Point(pos.x + int(size * 1.5), arms_y)
    )
    arms.draw(win)

    legs_y_end = body_y_end + int(size * 1.5)
    right_leg = Line(Point(pos.x, body_y_end), Point(pos.x + size, legs_y_end))
    right_leg.draw(win)
    left_leg = Line(Point(pos.x, body_y_end), Point(pos.x - size, legs_y_end))
    left_leg.draw(win)


def draw_stick_figure_family():
    win = Window()
    draw_stick_figure(win, 40, Point(80, 120))
    draw_stick_figure(win, 35, Point(200, 145))
    draw_stick_figure(win, 20, Point(300, 210))
    draw_stick_figure(win, 15, Point(360, 235))

    win.get_mouse()
