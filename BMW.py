import turtle
import turtle as t
t.setpos(0,-250)
t.pensize(8)
t.fillcolor("black")
t.begin_fill()
t.pencolor("gray")
t.circle(250)
t.end_fill()

t.pensize(3)
t.up()
t.setpos(0,-150)
t.down()
t.fillcolor("white")
t.begin_fill()
t.circle(150)
t.end_fill()
t.fillcolor("skycolor")
t.begin_fill()
t.circle(150, 90)
t.left(90)
t.pensize(2)
t.pencolor("black")
t.forward(150)
t.left(90)
t.forward(150)
t.end_fill()
t.up()
t.setpos(-150,0)
t.down()
t.begin_fill()
t.pensize(3)
t.pencolor("gray")
t.circle(150,-90)
t.left(90)
t.pensize(2)
t.pencolor("black")
t.forward(150)
t.right(90)
t.forward(150)
t.end_fill()

t.pensize(12)
t.pencolor("white")

t.up()
t.setpos(0,0)
t.right(35)
t.forward(165)
t.right(5.2)
t.down()
t.forward(64)
t.right(90)
t.forward(35)
t.circle(-16,180)
t.forward(35)
t.right(180)
t.forward(35)
t.circle(-16,180)
t.forward(35)

t.up()
t.setpos(-32,165)
t.setheading(90)
t.down()
t.forward(62)
t.setpos(0,180)
t.setpos(32,227)
t.right(180)
t.forward(62)

t.up()
t.setpos(0,0)
t.setheading(52)
t.forward(228)
t.down()
t.right(170)
t.forward(65)
t.left(142)
t.forward(50)
t.right(142)
t.forward(50)
t.left(142)
t.forward(65)

t.hideturtle()
t.done()
t.mainloop()

