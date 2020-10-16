import turtle

WIDTH, HEIGHT = 800, 600
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor('black')
screen.delay(0)

turtle.hideturtle()
turtle.tracer(0)

leo = turtle.Turtle()
leo.pensize(1)
leo.speed(0)
leo.setpos(0, -HEIGHT // 2)
leo.color('green')

gens = 7
axiom = 'XY'

rules = { 'F' : 'FF', \
        'X' : 'F[+X]F[-X]+X', \
        'Y' : 'Y', \
        '-' : '-', \
        '+' : '+', \
        '[' : '[', \
        ']' : ']'}

step = 8 / (gens / 2)
angle = 22.5

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
turtle.goto(-WIDTH // 2 + 60, HEIGHT // 2 - 100)
turtle.clear()

axiom = get_result(gens, axiom)
leo.left(90)
for ch in axiom:
    if ch == 'F':
        leo.forward(step)
    elif ch == '+':
        leo.right(angle)
    elif ch == '-':
        leo.left(angle)
    elif ch == '[':
        angle_, pos_ = leo.heading(), leo.pos()
        stack.append((angle_, pos_))
    elif ch == ']':
        angle_, pos_ = stack.pop()
        leo.setheading(angle_)
        leo.penup()
        leo.goto(pos_)
        leo.pendown()

screen.exitonclick()


