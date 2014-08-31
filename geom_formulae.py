__author__ = 'thabo'

from numpy import*
from numbers import Number
import math
def circle_area(radius):
    """
    Calculate the area of a circle from radius
    @param radius:length of radius of circle
    @return:area (units^2 from radius)
    >>> circle_area(8)
201.06
    """
    return pi*radius*radius
print (circle_area(8))

def circle_circumference(radius):
    """
    @param radius: length of radius of circle
    @return:circumference (units from radius of circle)
    >>> circle_circumference (8)
    50.26
    """
    return 2*pi*radius
print (circle_circumference(8))

def circle_circumference(diameter):
    """

    @param diameter: length of diameter of circle
    @return: circumference (units from diameter)
    >>> circle_circumference(16)
    50.26
    """
    return pi*diameter
print(circle_circumference(16))


def trapezium_area(a,b,height):
    """

    @param a: length of upper side or lower side of trapezium
    @param b: length of upper side or lower side of trapezium
    @param height: height of trapezium
    @return:area (units^2 from height of trapezium)
    >>> trapezium_area(2,3,4)
10
    """
    return (1/2)*(a+b)*height
print (trapezium_area(2,3,4))

def triangle_area(base,height):
    """

    @param base: length of triangle base
    @param height: height of triangle
    @return: area (units^2 from base or height)
     >>> triangle_area(2,3)
     3
    """
    return (1/2)*base*height
print (triangle_area(2,3))

def triangle_area(side,adjacent_side,angle):
    """

    @param side: length of any side
    @param adjacent_side: length of adjacent side
    @param angle: angle between the sides
    @return: area (units^2 from side)
    >>> triangle_area(4,5,60)

    """
    return (1/2)*side*adjacent_side*sin(math.radians(angle))
print(triangle_area(4,5,60))

def cube_area(side):
    """
    @param side: length of side of cube
    @return:area (unit^2 from side)
    >>> cube_area(4)
    96

    """
    return 6*(side*side)
print (cube_area(4))

def cylinder_volume(radius,height):
    """

    @param radius: length of radius of cylinder
    @param height: height of cylinder from one end to another
    @return:volume (units^3 units of radius or height)
    >>> cylinder_volume(3,6)
    169.59
    """
    return pi*height*(radius*radius)
print(cylinder_volume(3,6))

def cone_volume(radius,height):
    """

    @param radius: length of radius of cone
    @param height: height of cone from base to top
    @return: volume(units^3 from height or radius
    >>> cone_volume(4,4)
67.02
    """
    return (1/3)*height*pi*(radius*radius)
print (cone_volume(4,4))

def sphere_volume(radius):
    """

    @param radius: length of radius of sphere
    @return: volume (units^3 from radius)
    >>> sphere_volume(7)
    1436.76
    """
    return (4/3)*pi*(radius*radius*radius)
print (sphere_volume(7))

def rectangular_prism_volume(length,width,height):
    """

    @param length: length of base of prism
    @param width: width of base of prism
    @param height: height of prism from base to top
    @return:volume (units^3 from length,width or height)
    >>> rectangular_prism_volume(2,3,4)
    24
    """
    return length*width*height
print(rectangular_prism_volume(2,3,4))

def rectangular_pyramid_volume(length,width,height):
    """
    @param length: length of the base of the pyramid
    @param width:  width of base of pyramid
    @param height: height of pyramid from base to top
    @return: volume(units^3 from length,width or height)
    >>> rectangular_pyramid_volume(3,4,5)
    20
    """
    return (1/3)*length*width*height
print(rectangular_pyramid_volume(3,4,5))

def square_pyramid_surface_area(side,slant_height):
    """

    @param side: length of the side of base
    @param slant_height: height of each triangular face from the base to the top
    @return: surface area(units^2 from side)
    >>> square_pyramid_surface_area(4,4)
    48

    """
    return 2*side*slant_height+(side*side)
print(square_pyramid_surface_area(4,4))

def square_pyramid_surface_area(side,height):
    """

    @param side: length of base side
    @param height: height from base to top
    @return:surface area(units^2 from side or height)
    >>>square_pyramid_surface_area(4,5)
59.08
    """
    return side**2+2*side*math.sqrt((side**2/4)+height**2)
print (square_pyramid_surface_area(4,5))










