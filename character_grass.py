from pico2d import *
#하나하나할때마다 커밋을해야함
open_canvas()

boy = load_image('character.png')

def move_rectangle():
    print("Moving rectangle")
    pass
def move_circle():
    print("Moving circle")
    clear_canvas_now()
    boy.draw_now(400,300)
    #무조건 now로 만들기
    delay(0.1)
    pass

while True:
    #함수명을 이해가 가도록 적어야함
    move_circle()
    move_rectangle()
    #break
    pass

close_canvas()
