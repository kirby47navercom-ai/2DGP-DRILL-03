from pico2d import *
import math
#하나하나할때마다 커밋을해야함
open_canvas()

boy = load_image('character.png')

def move_top():
    pass
def move_right():
    pass
def move_bottom():
    pass
def move_left():
    pass


def move_rectangle():
    print("Moving rectangle")
    move_top()
    move_right()
    move_bottom()
    move_left()
    pass
def move_circle():
    print("Moving circle")
    r=200
    for i in range(0,360):
        clear_canvas_now()
        x = 400 +r* math.cos(math.radians(i))
        y = 300 +r* math.sin(math.radians(i))
        clear_canvas_now()
        boy.draw_now(x,y)
        #무조건 now로 만들기
        delay(0.01)
    pass

while True:
    #함수명을 이해가 가도록 적어야함
    move_circle()
    move_rectangle()
    #break
    pass

close_canvas()
