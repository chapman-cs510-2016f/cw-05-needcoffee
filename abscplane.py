#!/usr/bin/env python3

from abc import ABC, abstractmethod

"""CS510 - CW05 Abstract Base Classes.

This module provides abstract base classes for CW05.
Note that such a class does nothing by itself: all functionality
is just a pass statement as written. Instead, a coder is
intended to inherit from this class in order to adopt its
interface. The set of attributes and methods of a class
that subclasses the abstract base class should provide
implementations as appropriate.

The point of such a structure is to guide other programmers
into good design, so that they can use an interface that
you expect to exist. This is part of the communal nature of
coding. Your code does not exist in a vacuum. It exists in
a community of other coders that are all sharing code with
each other. Without proper communication on what people 
expect from each other, it devolves into chaos.
"""

class AbsComplexPlane(ABC):
    """Abstract base class for complex plane.
    
    A complex plane is a 2D grid of complex numbers, having
    the form (x + y*1j), where 1j is the unit imaginary number in
    Python, and one can think of x and y as the coordinates for
    the horizontal axis and the vertical axis of the plane, 
    respectively. Recall that (1j)*(1j) == -1. Also recall that 
    the FOIL rule for multiplication still works:
        (x + y*1j)*(v + w*1j) = (x*v - y*w + (x*w + y*v)*1j)
    You can check these results in an interpreter.
    
    We will explore several implementations for a complex plane in
    this course, so we wish to have an abstract interface that
    is independent of any particular implementation.
    
    In addition to generating the 2D grid of numbers (x + y*1j),
    we wish to easily support transformations of the plane with
    an arbitrary function f. Done properly, the attribute self.plane
    should store a 2D grid of numbers f(x + y*1j) such that the
    parameter x ranges from self.xmin to self.xmax with self.xlen
    total points, while the parameter y ranges from self.ymin to
    self.ymax with self.ylen total points. By default, the function
    f should be the identity function lamdax:x, which does nothing to
    the bare complex plane.
    
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
    
    # Class attributes, to be set during an __init__
    xmin  = NotImplemented
    xmax  = NotImplemented
    xlen  = NotImplemented
    ymin  = NotImplemented
    ymax  = NotImplemented
    ylen  = NotImplemented
    # The implementation type of plane is up to the user
    plane = NotImplemented
    # Note that the default f should be the identity: id
    f     = NotImplemented
    
    # The @abstractmethod "decorator" forces all subclasses
    # to provide implementations for the following method
    @abstractmethod
    def refresh(self):
        """Regenerate complex plane.
        For every point (x + y*1j) in self.plane, replace
        the point with the value self.f(x + y*1j). 
        """
        pass
    
    @abstractmethod
    def zoom(self):
        """Reset self.xmin, self.xmax, and/or self.xlen.
        Also reset self.ymin, self.ymax, and/or self.ylen.
        Zoom into the indicated range of the x- and y-axes.
        Refresh the plane as needed."""
        pass
    
    @abstractmethod
    def set_f(self):
        """Reset the transformation function f.
        Refresh the plane as needed."""
        pass

