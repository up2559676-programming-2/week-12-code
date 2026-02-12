import math
import random

from graphix import Circle, Line, Point, Rectangle, Text, Window

from pract5 import distance_between_points

# Remember to update the line above if you are using other Graphix objects


def greet(name):
    print("Hello", name + ".")
    if len(name) > 20:
        print("That's a long name!")


def can_you_vote(age):
    if age >= 18:
        print("You can vote")
    else:
        print("Sorry, you can't vote")


def get_degree_class(mark):
    if mark >= 70:
        return "1st"
    elif mark >= 60:
        return "2:1"
    elif mark >= 50:
        return "2:2"
    elif mark >= 40:
        return "3rd"
    else:
        return "Fail"


# We will simplify this function later in the term
def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def days_in_month(month, year):
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    else:
        return 31


def overly_complex_days_in_month(month, year):
    if (
        month == 1
        or month == 3
        or month == 5
        or month == 7
        or month == 8
        or month == 10
        or month == 12
    ):
        return 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif is_leap_year(year):
        return 29
    else:
        return 28


def count_down():
    for i in range(10, 0, -1):
        print(i, "...", end=" ")
    print("Blast Off!")


def numbered_triangle(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


def draw_circle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.fill_colour = colour
    circle.outline_colour = colour
    circle.draw(win)


def fast_food_order_price():
    price = float(input("Enter price of order: "))
    if price < 20:
        price += 2.5

    print(f"The total price of your order is {price}")


def what_to_do_today(temp: float) -> str:
    activity = "shopping in Gunwharf Quays"
    if temp > 25:
        activity = "swim in the sea"
    elif temp < 10:
        activity = "watch movie at home"

    return activity


def display_square_roots(start: int, end: int):
    for n in range(start, end + 1):
        print(f"The square root of {n} is {math.sqrt(n):.3f}")


def calculate_grades(mark: int) -> str:
    if 20 < mark < 0:
        return "X"

    if mark >= 16:
        return "A"
    elif mark >= 12:
        return "B"
    elif mark >= 8:
        return "C"
    else:
        return "F"


def peas_in_a_pod():
    pea_radius = 50
    pea_diameter = pea_radius * 2
    num_peas = int(input("Enter the number of peas in a pod: "))

    win = Window(width=num_peas * pea_diameter, height=pea_diameter)

    for i in range(num_peas):
        pea = Circle(Point(i * pea_diameter + pea_radius, pea_radius), pea_radius)
        pea.fill_colour = "green"
        pea.draw(win)

    win.get_mouse()


def ticket_price(dist: int, age: int) -> float:
    base_price = 10.0
    dist_mult = 0.15
    age_discount = 0.4

    price = base_price + dist * dist_mult

    if 60 <= age <= 15:
        return price * (1 - age_discount)

    return price


def numbered_square(n: int):
    for i in range(n, 0, -1):
        s = " ".join(str(j) for j in range(i, i + n))
        print(s)


def draw_coloured_eye(win: Window, centre: Point, radius: int, colour: str):
    eye_radius = [radius, radius // 2, radius // 4]
    eye_colours = ["white", colour, "black"]

    for radius, colour in zip(eye_radius, eye_colours):
        circle = Circle(centre, radius)
        circle.fill_colour = colour
        circle.outline_width = 2
        circle.draw(win)


def eye_picker():
    win = Window()

    xcord = int(input("Enter x coord of the eye: "))
    if 0 > xcord > win.width:
        print("eye centre not in window")
        return

    ycord = int(input("Enter y coord of the eye: "))
    if 0 > ycord > win.height:
        print("eye centre not in window")
        return

    radius = int(input("Enter the radius of the eye: "))
    colour = input("Enter the colour of the eye: ")
    if colour not in ("blue", "grey", "green", "brown"):
        print("not a valid eye colour")
        return

    draw_coloured_eye(win, Point(xcord, ycord), radius, colour)


def draw_patch_design_0(win: Window):
    for i in range(5):
        for j in range(5):
            if i == 0 and j != 0:
                line = Line(Point(20 * j, 0), Point(20 * j, 100))
                line.outline_colour = "red"
                line.draw(win)

            text = Text(Point(20 * j + 10, 20 * i + 10), "hi!")
            text.fill_colour = "red"
            text.size = 8
            text.draw(win)

        if i != 0:
            line = Line(Point(0, i * 20), Point(100, i * 20))
            line.outline_colour = "red"
            line.draw(win)


def draw_patch_design_1(win: Window):
    for i in range(0, 101, 20):
        line = Line(Point(i * 20, 0), Point(100, 100 - i * 20))
        line.outline_colour = "red"
        line.draw(win)

        line = Line(Point(i * 20, 0), Point(0, i * 20))
        line.outline_colour = "red"
        line.draw(win)

        line = Line(Point(i * 20, 100), Point(0, 100 - i * 20))
        line.outline_colour = "red"
        line.draw(win)

        line = Line(Point(i * 20, 100), Point(100, i * 20))
        line.outline_colour = "red"
        line.draw(win)


def draw_patch_design_2(win: Window):
    for i in range(0, 50, 5):
        rect = Rectangle(Point(i, i), Point(100 - i, 100 - i))
        num = i // 5
        if num % 2 == 0:
            rect.fill_colour = "red"
            rect.outline_colour = "red"
        else:
            rect.fill_colour = "white"
            rect.outline_colour = "white"
        rect.draw(win)


def draw_patch_design_3(win: Window):
    for i in range(0, 100, 10):
        rect = Rectangle(Point(90 - i, i), Point(100, i + 10))
        rect.fill_colour = "red"
        rect.outline_colour = "red"
        rect.draw(win)


def draw_patch_design_4(win: Window):
    for i in range(0, 100, 10):
        rect = Rectangle(Point(90 - i, i), Point(100 - i, i + 10))
        rect.fill_colour = "red"
        rect.outline_colour = "red"
        rect.draw(win)


def draw_patch_design_5(win: Window):
    for i in range(0, 101, 10):
        line = Line(Point(i, 0), Point(100 - i, 100))
        line.outline_colour = "red"
        line.draw(win)

        line = Line(Point(0, i), Point(100, 100 - i))
        line.outline_colour = "red"
        line.draw(win)


def draw_patch_design_6(win: Window, x: int, y: int, colour: str):
    for i in range(10, 101, 10):
        circle = Circle(Point(50 + x, (100 - i // 2) + y), i // 2)
        circle.outline_colour = colour
        circle.draw(win)


def draw_patch_design_7(win: Window):
    for i in range(10, 100, 20):
        for j in range(4):
            circle = Circle(Point(i, 10 + j * 20), 10)
            circle.outline_colour = "red"
            if j % 2 == 0:
                circle.fill_colour = "red"
            circle.draw(win)


def draw_patch_design_8(win: Window):
    for i in range(9):
        rect = Rectangle(Point(0, 10), Point(90, 100))
        rect.fill_colour = "red"
        rect.outline_colour = "red"
        rect.draw(win)


def draw_patch_design_9(win: Window):
    for i in range(10, 101, 10):
        line = Line(Point(i, 0), Point(100, i))
        line.fill_colour = "red"
        line.draw(win)

    for i in range(10, 101, 10):
        line = Line(Point(0, i), Point(i, 100))
        line.fill_colour = "red"
        line.draw(win)


def draw_patchwork():
    win = Window(width=300, height=200)

    for y in range(0, win.height, 100):
        for x in range(0, win.width, 100):
            print(x, y)
            draw_patch_design_6(win, x, y, "blue")

    win.get_mouse()


def eyes_all_around():
    colours = ["blue", "grey", "green", "brown"]

    win = Window(width=500, height=500)

    for i in range(30):
        centre = win.get_mouse()
        draw_coloured_eye(win, centre, 30, colours[i % len(colours)])

    win.get_mouse()


def archery_game():
    margin = 20

    win = Window()
    width = win.width
    height = win.height

    centre = Point(width // 2, height // 2)

    blue_rad = height // 2 - margin
    yellow_rad = blue_rad // 3
    red_rad = yellow_rad * 2

    draw_circle(win, centre, blue_rad, "blue")
    draw_circle(win, centre, red_rad, "red")
    draw_circle(win, centre, yellow_rad, "yellow")

    for i in range(5):
        raw_aim = win.get_mouse()
        aim = Point(raw_aim.x + random.randint(1, 5), raw_aim.y + random.randint(1, 5))

        dist = abs(distance_between_points(centre, aim))  # type: ignore
        print(dist)

        circle = Circle(aim, 3)
        circle.fill_colour = "black"
        circle.draw(win)

    win.get_mouse()


if __name__ == "__main__":
    archery_game()
