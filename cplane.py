#!/usr/bin/env python3

import abscplane

"""
Module docstring and stuff
"""
class ComplexPlane(object):
 
    def __init__(self, xmin, xmax, xlen, ymin, ymax, ylen):
        self.xmin = xmin
        self.xmax = xmax
        self.xlen = xlen
        self.xtick = (xmax - xmin)/(xlen - 1.0)
        self.ymin = ymin
        self.ymax = ymax
        self.ylen = ylen
        self.ytick = (ymax - ymin)/(ylen - 1.0)
        self.f = lambda x:x
        
        self.plane = []
        for imaginary in [self.ymax - self.ytick*i for i in range(self.ylen)]:
            self.plane.append([(real+1j*imaginary) for real in [self.xmin + self.xtick*i for i in range(self.xlen)]])

    def refresh(self):
        """Regenerate complex plane.
        For every point (x + y*1j) in self.plane, replace
        the point with the value self.f(x + y*1j). 
        """
        for real in range(self.xlen):
            for imaginary in range(self.ylen):
                self.plane[real][imaginary] = self.f(self.plane[real][imaginary])

    def zoom(self, xmin, xmax, xlen, ymin, ymax, ylen):
        """Reset self.xmin, self.xmax, and/or self.xlen.
        Also reset self.ymin, self.ymax, and/or self.ylen.
        Zoom into the indicated range of the x- and y-axes.
        Refresh the plane as needed."""

        function = self.f
        self.__init__(xmin, xmax, xlen, ymin, ymax, ylen)
        self.set_f(function)
        


    def set_f(self, function):
        """Reset the transformation function f.
        Refreshes the plane after setting f to function."""
        self.f = function
        self.refresh()
