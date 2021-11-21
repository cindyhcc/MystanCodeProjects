"""
File: sierpinski.py
Name: Cindy Huang
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	This program draws a Sierpinski triangle with GLine on GWindow based on the order input given by users.
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: variable to control how many
	:param length: Length of each side of the triangle
	:param upper_left_x: location of the upper left x point of each triangle
	:param upper_left_y: location of the upper left y axis of each triangle
	:return: Sierpinski triangle
	"""
	# define base case
	if order == 0:
		pass
	else:
		# Draw Sierpinski triangle when order = 1
		if order == 1:
			base = GLine(upper_left_x, upper_left_y, upper_left_x+length, upper_left_y)
			left_side = GLine(upper_left_x, upper_left_y, upper_left_x+length*.5, upper_left_y+length*.866)
			right_side = GLine(upper_left_x+length, upper_left_y, upper_left_x+length-length*.5, upper_left_y+length*.866)
			window.add(base)
			window.add(left_side)
			window.add(right_side)
		else:
			# Draw Sierpinski triangle  depending on the order given by user
			base = GLine(upper_left_x, upper_left_y, upper_left_x+length, upper_left_y)
			# Draw left side of triangle
			left_side = GLine(upper_left_x, upper_left_y, upper_left_x+length*.5, upper_left_y+length*.866)
			# Draw right side of triangle
			right_side = GLine(upper_left_x+length, upper_left_y, upper_left_x+length-length*.5, upper_left_y+length*.866)
			# Add triangle to window
			window.add(base)
			window.add(left_side)
			window.add(right_side)
			# Identify self similarity
			sierpinski_triangle(order-1, length/2, upper_left_x, upper_left_y)
			sierpinski_triangle(order-1, length/2, upper_left_x+length/2, upper_left_y)
			sierpinski_triangle(order-1, length/2, upper_left_x+length*.25, upper_left_y+length/2*.866)
			pause(500)


if __name__ == '__main__':
	main()