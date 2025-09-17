import math
from pico2d import *

open_canvas()

boy = load_image('character.png')

def move_in_rectangle():
    points = [(100, 100), (700, 100), (700, 500), (100, 500)]
    for i in range(4):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % 4]
        for t in range(0, 100, 2):
            x = x1 + (x2 - x1) * t / 100
            y = y1 + (y2 - y1) * t / 100
            clear_canvas()
            boy.draw(x, y)
            update_canvas()
            delay(0.01)

def move_in_triangle():
    points = [(400, 550), (700, 150), (100, 150)]
    for i in range(3):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % 3]
        for t in range(0, 100, 2):
            x = x1 + (x2 - x1) * t / 100
            y = y1 + (y2 - y1) * t / 100
            clear_canvas()
            boy.draw(x, y)
            update_canvas()
            delay(0.01)

def move_in_circle():
    cx, cy, r = 400, 300, 200
    for degree in range(0, 360, 2):
        rad = math.radians(degree)
        x = cx + r * math.cos(rad)
        y = cy + r * math.sin(rad)
        clear_canvas()
        boy.draw(x, y)
        update_canvas()
        delay(0.01)

while True:
    move_in_rectangle()
    move_in_triangle()
    move_in_circle()

close_canvas()
