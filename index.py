import turtle

tur = turtle.Turtle()
# tur.filling()
tur.color("red")
tur.begin_fill()

for _ in range(2):

	tur.forward(50)
	tur.right(90)
	tur.forward(200)
	tur.right(90)
tur.end_fill()
tur.begin_fill()
tur.right(65)
tur.forward(225)
tur.left(65)
tur.forward(50)
tur.left(115)
tur.forward(225)
tur.left(65)
tur.forward(50)
tur.end_fill()
tur.right(245)
tur.forward(225)
tur.begin_fill()
tur.left(65)
tur.forward(50)
tur.left(90)
tur.forward(205)
tur.left(90)
tur.forward(50)
tur.left(90)
tur.forward(200)
tur.end_fill()









screen  = turtle.Screen()
screen.exitonclick()