'''Draws a Circle using turtle module'''

# Import turtle
import turtle

def draw_circle():
	'''Draws a Circle'''
	window = turtle.Screen()
	window.bgcolor('orange')

	angie = turtle.Turtle()
	angie.shape('arrow')
	angie.color('blue')
	angie.circle(100)

draw_circle()