'''Draws a Square using turtle module'''

# Import turtle
import turtle

def draw_square():
	'''Draw a Square'''
	window = turtle.Screen()
	window.bgcolor('green')

	sq = turtle.Turtle()
	sq.shape('turtle')
	sq.color('yellow')

	for i in range(1,5):
		sq.forward(100)
		sq.right(90)

draw_square()