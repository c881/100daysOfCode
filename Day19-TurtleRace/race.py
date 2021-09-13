import turtle as t

turtles = []
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']

scr = t.Screen()
scr.setup(width=500,height=400)
new_y = -120

for color in colors:
    turtles.append(t.Turtle(shape='turtle'))
    turtles[-1].penup()
    turtles[-1].color(color)
    turtles[-1].goto(x=-230, y=new_y )
    new_y += 40


scr.exitonclick()
