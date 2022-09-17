a=100
b=50
import turtle 
t= turtle.Turtle()
t.up()
t.goto(a,a)
t.down()
t.color("red")
t.begin_fill()
t.circle(a)
t.end_fill()

t.up()
t.goto(0,a)
t.down()
t.color("blue")
t.circle(a)

t.up()
t.goto(-a,a)
t.down()
t.circle(a)

t.up()
t.goto(a,-b)
t.down()
t.circle(a)

t.up()
t.goto(-a,-b)
t.down()
t.circle(a)
