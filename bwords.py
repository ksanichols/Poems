#!/usr/bin/python
import turtle as t

turtle = t.RawTurtle(t.Screen())
turtle.hideturtle()
turtle.pu()
turtle.speed(2)
origin = [turtle.xcor(), turtle.ycor()]

poem = "bee words buzz on through \n" + \
       "sea words sigh and mew \n" + \
       "but fondest? the words that follow me\n" + \
       "home      held there by you      \n    \n        " 

angle = 2
for letter in poem:
    if letter == "\n":
        turtle.setpos(origin[0], origin[1] + 10)
        origin[1] += 10
        turtle.seth(0)
    turtle.fd(10)
    turtle.write(letter)
    turtle.rt(angle)
    angle -= 0.01
