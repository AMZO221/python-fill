from turtle import*
speed(12)
hideturtle()
color('red')
bgcolor('black')
p = True
n = 1
while(True):
    circle(n)
    if p:
        n = n-1
        color('white')
    else:
        n = n+1
        color('red')
    if n == 0 or n == 60:
        p = not p
        color('aqua')
    left (1)
    forward(3)