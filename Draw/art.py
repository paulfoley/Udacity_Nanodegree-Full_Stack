'''Draws Art using turtle module'''

# Import turtle
import turtle

def draw_art():
	'''Draw Art'''
	window = turtle.Screen()
	window.bgcolor('red')
	
	brad = turtle.Turtle()
	brad.shape('turtle')
	brad.color('green')
	brad.speed(10)

	for i in range(1,37):
		draw_triangle(brad)
		brad.right(10)

draw_art()