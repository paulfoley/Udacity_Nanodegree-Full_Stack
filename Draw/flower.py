'''Draws a flower using turtle module'''

# Import turtle
import turtle

def draw_flower():
	'''Draw a flower'''
	window = turtle.Screen()
	window.bgcolor("blue")

	icon =turtle.Turtle()
	icon.shape("turtle")
	icon.color("orange")
	icon.speed(20)

	for i in range(1,37):
		icon.left(35)
		icon.forward(50)
		icon.right(35)
		icon.forward(50)
		icon.right(145)
		icon.forward(50)
		icon.right(35)
		icon.forward(50)
		icon.right(10)

	icon.seth(270)
	icon.forward(200)

	window.exitonclick()

draw_flower()
