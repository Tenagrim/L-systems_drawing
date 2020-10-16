import turtle
from random import randint

WIDTH, HEIGHT = 1200, 700
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor('black')
screen.delay(0)

turtle.hideturtle()
turtle.tracer(0)

leo = turtle.Turtle()
leo.pensize(1)
leo.speed(0)
leo.setpos(0, -HEIGHT // 2 + 40)
leo.color('green')

gens = 14
axiom = 'XY'

rules = {'X' : 'F[@[-X]+X]', \
        'Y' : 'Y', \
        'F' : 'F', \
        '-' : '-', \
        '+' : '+', \
        '[' : '[', \
        ']' : ']', \
        '@' : '@'}

step = 80
angle = lambda: randint(0,35)
color = [0.35, 0.2, 0.0]
thickness = 20

def apply_rules(axiom):
    print(">>>"+axiom)
    axiTemp = ""
    for ch in axiom:
        axiTemp += rules[ch]
    return axiTemp

def get_result(gens, axiom):
    for gen in range(gens):
        axiom = apply_rules(axiom)
    return axiom

stack = []

turtle.pencolor('white')
#turtle.goto(-WIDTH // 2 + 60, HEIGHT - 200 )
turtle.clear()

axiom = get_result(gens, axiom)
leo.left(90)
leo.pensize(thickness)
for ch in axiom:
    leo.color(color)
    if ch == 'F' or ch == 'X':
        leo.forward(step)
    elif ch == '@':
        step -= 6
        step = max(2, step)
        color[1] += 0.04
        thickness *= 0.65
        thickness = max(1, thickness)
        leo.pensize(thickness)
    elif ch == '+':
        leo.right(angle())
    elif ch == '-':
        leo.left(angle())
    elif ch == '[':
        angle_, pos_ = leo.heading(), leo.pos()
        stack.append((angle_, pos_, thickness, step, color[1]))
    elif ch == ']':
        angle_, pos_, thickness, step, color[1] = stack.pop()
        leo.pensize(thickness)
        leo.setheading(angle_)
        leo.penup()
        leo.goto(pos_)
        leo.pendown()

screen.exitonclick()


