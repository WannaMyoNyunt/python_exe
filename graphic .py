from cmath import rect
import turtle

screen = turtle.Screen()
screen.bgcolor("blue")
screen.title("My first graph")

t = turtle.Turtle()
t.color("white")
t.shape("turtle")
t.speed(1)

r=30



t.penup()
t.goto(-60, -30)
t.pendown()
t.circle(r)
    

t.penup()
t.goto(0,-30)
t.pendown()
t.circle(r)

t.penup()
t.goto(-30,30)
t.pendown()


t.forward(10)
t.left(90)
t.forward(120)
t.left(90)
t.forward(30)
t.left(90)
t.forward(120)
