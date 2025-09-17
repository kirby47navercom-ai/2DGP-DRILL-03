from pico2d import *
import math
#하나하나할때마다 커밋을해야함
#리펙터링(refactor) -> 메서드 추출(extract method) 복사한 것을 함수로 만들 수 있음
#코딩에서 내가 만든 구현 결과가 제대로 됐는지에 대한 걸린시간 테스트 리드 타임
#코파일럿을 사용하되 사용만 하지마라
#가장 큰 부분을 만들려면 작게작게 커밋하면서해야된다
#하수는 만들고 나중에 함수를 호출
#고수는 함수호출을 먼저하고 그다음 정의한다
#테스리드타임을 줄여야한다() 걸리는 시간 자체를 줄이라는 말
open_canvas()

boy = load_image('character.png')

def move_top():
    print('Moving top')
    for y in range(100,500,5):
        draw_boy(750,y)
    pass
def move_right():
    print('Moving right')
    for x in range(400,750,5):
        draw_boy(x,100)
    pass
def move_bottom():
    print('Moving bottom')
    for y in range(500, 100, -5):
        draw_boy(50, y)
    pass
def move_left():
    print('Moving left')
    for x in range(750, 50, -5):
        draw_boy(x, 500)
    pass
def move_go():
    print('Moving go')
    for x in range(400,750,5):
        draw_boy(x,100)
    pass

def move_rectangle():
    print("Moving rectangle")
    move_go()
    move_top()
    move_left()
    move_bottom()
    move_right()
    pass
def move_circle():
    print("Moving circle")
    r=200
    for i in range(-90,270):
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
