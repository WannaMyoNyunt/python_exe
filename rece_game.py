import turtle
import random
import time

def turtle_race():

    screen = turtle.Screen()
    screen.bgcolor("lightblue")
    screen.title("5 turtles race game")



    #create race track
    track = turtle.Turtle()
    track.speed(0)
    track.penup()
    #start line
    track.goto(-300, 150)
    track.pendown()
    track.color("red")
    track.width(3)
    track.goto(-300, -150)
    #end line
    track.penup()
    track.goto(300, 150)
    track.pendown()
    track.color("blue")
    track.width(3)
    track.goto(300, -150)

    #create turtles

    colors= ["Red", "Blue", "Green", "Blue"]
    turtles = []

    for i, color in enumerate(colors):
        t = turtle.Turtle()
        t.shape("turtle")
        t.color(color) 
        t.penup()
        t.goto(-320,80 - i*50)
        turtles.append(t)
        
        #countdown
    countdown = turtle.Turtle()
    countdown.penup()
    countdown.hideturtle()
    countdown.goto(0,200)
    
    for i in range(3,0,-1):
        countdown.write(str(i), align="center", font=("Arial", 48, "normal"))
        time.sleep(1)
        countdown.clear()
        
    countdown.write("Min Thu Swe SPAW!", align="center", font=("Arial", 48, "normal"))
    time.sleep(0.5)
    countdown.clear()
    
    #Race
    
    winner = None
    while not winner:
        for t in turtles:
            distance = random.randint(1,10)
            t.forward(distance)
            
            #check for winner
            if t.xcor() >= 300:
                winner = t
                break
            
    #Announce winner
    countdown.goto(0,0)
    countdown.color(winner.color()[0])
    countdown.write(f"{winner.color()[0]} Turtle Wins!", align="center", font=("Arial", 36, "normal"))

    screen.mainloop()
    
turtle_race()