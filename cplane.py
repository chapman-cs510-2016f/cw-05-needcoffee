#!/usr/bin/env python3

import abscplane

"""
Implementation for Abstract Base Class AbsComplexPlane
A complex plane is a 2D grid of complex numbers, having
the form (x + y*1j), where 1j is the unit imaginary number,
and one can think of x and y as the coordinates for
the horizontal axis and the vertical axis of the plane, 
respectively.
"""

class ComplexPlane(abscplane.AbsComplexPlane):
	"""Create and manipulate a complex plane
	In addition to generating the 2D grid of numbers (x + y*1j),
	the class supports transformations of the plane with
	an arbitrary function f. The attribute self.plane
	stores a 2D grid of numbers f(x + y*1j) such that the
	parameter x ranges from self.xmin to self.xmax with self.xlen
	total points, while the parameter y ranges from self.ymin to
	self.ymax with self.ylen total points. By default, the function
	f is the identity function lamdax:x, which does nothing to
	the bare complex plane. Under this function, the plane is
	organized to look like the mathematical complex plane, so
	that real values inrease from left to right, and imaginary
	values decrease from top to bottom.
    
	Attributes:
		xmax (float) : maximum horizontal axis value
		xmin (float) : minimum horizontal axis value
		xlen (int)   : number of horizontal points
		ymax (float) : maximum vertical axis value
		ymin (float) : minimum vertical axis value
		ylen (int)   : number of vertical points
		plane        : stored complex plane implementation
		f    (func)  : function displayed in the plane
	"""
 
	def __init__(self, xmin, xmax, xlen, ymin, ymax, ylen):
		"""__init__ constructor to create ComplexPlane object
	
		Args:
			xmax (float) : maximum horizontal axis value
			xmin (float) : minimum horizontal axis value
			xlen (int)   : number of horizontal points
			ymax (float) : maximum vertical axis value
			ymin (float) : minimum vertical axis value
			ylen (int)   : number of vertical points
		"""

		self.xmin = xmin
		self.xmax = xmax
		self.xlen = xlen
		#xtick and ytick calculate distance between each point, not the number of points,
		#hence subtracting 1
		self.xtick = (xmax - xmin)/(xlen - 1.0) 
		self.ymin = ymin
		self.ymax = ymax
		self.ylen = ylen
		self.ytick = (ymax - ymin)/(ylen - 1.0)
		self.f = lambda x:x

		self.plane = []
		#Generates a list of imaginary components using ytick as a stepsize,
		#starting from the largest (top of plane) and counting down.
		#Then generates a list of real components using xtick as a stepsize,
		#starting from the smallest (left of plane) and counting up (right).
		#Then pairs each real component with each imaginary component,
		#creating a list of ascending lists of real components with the same imaginary component
		for imaginary in [self.ymax - self.ytick*i for i in range(self.ylen)]:
			self.plane.append([(real+1j*imaginary) for real in [self.xmin + self.xtick*i for i in range(self.xlen)]])

	def refresh(self):
		"""Regenerate complex plane.
		For every point (x + y*1j) in self.plane, replace
		the point with the value self.f(x + y*1j). 
		"""

		for real in range(self.xlen):
			for imaginary in range(self.ylen):
				#goes through each point in the list of lists and applies f
				self.plane[imaginary][real] = self.f(self.plane[imaginary][real])

	def zoom(self, xmin, xmax, xlen, ymin, ymax, ylen):
		"""Reset self.xmin, self.xmax, and/or self.xlen.
		Also reset self.ymin, self.ymax, and/or self.ylen.
		Zoom into the indicated range of the x- and y-axes.
		Refresh the plane as needed.
		Args:
			xmax (float) : maximum horizontal axis value
			xmin (float) : minimum horizontal axis value
			xlen (int)   : number of horizontal points
			ymax (float) : maximum vertical axis value
			ymin (float) : minimum vertical axis value
			ylen (int)   : number of vertical points
		"""

		function = self.f #stores the attribute f before constructor call resets it
		self.__init__(xmin, xmax, xlen, ymin, ymax, ylen)
		self.set_f(function) #reapplies the function to the plane

	def set_f(self, function):
		"""Reset the transformation function f.
		Refreshes the plane after setting attribute 
		f to function.
		Args:
			function (function) : function to apply to 
				points of complex plane.
		"""

		#remake plane to get rid of f, otherwise new function applied on top of existing function
		self.__init__(self.xmin, self.xmax, self.xlen, self.ymin, self.ymax, self.ylen) 
		self.f = function
		self.refresh() #calls refresh to have function change take effect
