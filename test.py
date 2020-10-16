import turtle
from random import randint
from math import floor

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
leo.setpos(0, -HEIGHT // 2 + 50)
leo.color('green')

gens = 9
axiom = 'XY'

rules = { 'F' : 'F', \
        'X' : 'F[@[+X][FX]-X]', \
        'Y' : 'Y', \
        '-' : '-', \
        '+' : '+', \
        '[' : '[', \
        ']' : ']', \
        '@' : '@', \
        'Z' : 'Z'}

step = 80
def angle(i):
    return randint(0, max(2,60 - i))
color = [0.45, 0.2, 0.0]
thickness = 15

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
#turtle.goto(-WIDTH // 2 + 60, HEIGHT // 2 - 100)
turtle.clear()

axiom = get_result(gens, axiom)
leo.left(90)
leo.pensize(thickness)
i = -1
size = len(axiom)
percent = size // 10
cur = 0
for ch in axiom:
    if cur % percent == 0:
        print(str(floor(cur / size * 100)+1) +  '%')
    cur = cur + 1
    leo.color(color)
    if ch == 'F' or ch == 'X' or ch == 'Z':
        leo.forward(step)
    elif ch == '@':
        i = i + 1
        step *= 0.75
        #step = max(2, step)
        #thickness *= 0.65
        thickness *= 0.77
        color[1] += 0.04
        thickness = max(1, thickness)
        leo.pensize(thickness)
    elif ch == '+':
        leo.right(angle(i))
    elif ch == '-':
        leo.left(angle(i))
    elif ch == '[':
        angle_, pos_ = leo.heading(), leo.pos()
        stack.append((angle_, pos_, thickness, step, color[1], i))
    elif ch == ']':
        angle_, pos_, thickness, step, color[1], i = stack.pop()
        leo.pensize(thickness)
        leo.setheading(angle_)
        leo.penup()
        leo.goto(pos_)
        leo.pendown()

screen.exitonclick()


