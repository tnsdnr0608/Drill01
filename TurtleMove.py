import turtle

def turtle_move_w(): #turtle 위로 이동
    turtle.setheading(90)
    turtle.forward(90)
    turtle.stamp()
def turtle_move_s(): #turtle 아래로 이동
    turtle.setheading(-90)
    turtle.forward(90)
    turtle.stamp()
def turtle_move_a(): #turtle 왼쪽 이동
    turtle.setheading(180)
    turtle.forward(90)
    turtle.stamp()
def turtle_move_d(): #turtle 오른쪽 이동
    turtle.setheading(-360)
    turtle.forward(90)
    turtle.stamp()
def turtle_restart(): #esc를 눌러 재시작
    turtle.reset()
    
turtle.shape('turtle')
turtle.onkey(turtle_move_w, 'w')
turtle.onkey(turtle_move_s, 's')
turtle.onkey(turtle_move_a, 'a')
turtle.onkey(turtle_move_d, 'd')
turtle.onkey(turtle_restart, 'Escape')
turtle.listen()
