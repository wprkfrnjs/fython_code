import turtle

t=turtle.Turtle()

r= int(input ('반지름'))
#print(r)
#print(int(input ('반지름')))
c= input('색깔')

t.color(c)
t.begin_fill()
t.circle(r)
t.end_fill()
