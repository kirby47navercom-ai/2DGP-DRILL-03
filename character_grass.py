from pico2d import *
import math
#하나하나할때마다 커밋을해야함
#리펙터링(refactor) -> 메서드 추출(extract method) 복사한 것을 함수로 만들 수 있음
#코딩에서 내가 만든 구현 결과가 제대로 됐는지에 대한 걸린시간 테스트 리드 타임
open_canvas()

boy = load_image('character.png')

def move_top():
    print('Moving top')
    for x in range(0,800,5):
        draw_boy(x,550)
    pass
def move_right():
    print('Moving right')
    pass
def move_bottom():
    print('Moving bottom')
    pass
def move_left():
    print('Moving left')
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
        draw_boy(x, y)
    pass


def draw_boy(x: float, y: float):
    clear_canvas_now()
    boy.draw_now(x, y)
    # 무조건 now로 만들기
    delay(0.01)


while True:
    #함수명을 이해가 가도록 적어야함
    move_circle()
    move_rectangle()
    #break
    pass

close_canvas()
