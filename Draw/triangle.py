'''Draws a Triangle using turtle module'''

# Import turtle
import turtle

def draw_triangle():
	'''Draws a Triangle'''
	window = turtle.Screen()
	window.bgcolor('purple')

	tri = turtle.Turtle()
	tri.shape('turtle')
	tri.color('green')

	for i in range(1,4):
		tri.forward(150)
		tri.right(120)

draw_triangle()