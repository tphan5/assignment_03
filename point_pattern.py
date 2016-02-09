import math  # I am guessing that you will need to use the math module

"""
Below are 5 functions (we will talk about what
a function is later) that I have removed bits of
logic from.  The missing logic is noted with a comment.

The files tests.py runs units tests on these functions.
For this week, you should fill in the logic in these
functions so that the tests pass.
"""

def manhattan_distance(a, b):
    """
    Compute the Manhattan distance between two points

    Parameters
    ----------
    a : tuple
        A point in the form (x,y)

    b : tuple
        A point in the form (x,y)

    Returns
    -------
    distance : float
               The Manhattan distance between the two points
    """

    distance = abs(a[0] - b[0]) + abs(a[1] - b[1]) # Add the algorithm to compute manhattan distance here
    return distance


def euclidean_distance(a, b):
    """
    Compute the Euclidean distance between two points

    Parameters
    ----------
    a : tuple
        A point in the form (x,y)

    b : tuple
        A point in the form (x,y)

    Returns
    -------

    distance : float
               The Euclidean distance between the two points
    """
    distance = math.sqrt(((b[0] - a[0])**2) + ((b[1] - a[1])**2))  # Add the euclidean distance algorithm here
    return distance


def shift_point(point, x_shift, y_shift):
    """
    Shift a point by some amount in the x and y directions

    Parameters
    ----------
    point : tuple
            in the form (x,y)

    x_shift : int or float
              distance to shift in the x direction

    y_shift : int or float
              distance to shift in the y direction

    Returns
    -------
    new_x : int or float
            shited x coordinate

    new_y : int or float
            shifted y coordinate

    Note that the new_x new_y elements are returned as a tuple

    Example
    -------
    >>> point = (0,0)
    >>> shift_point(point, 1, 2)
    (1,2)
    """
    x = getx(point)
    y = gety(point)

    x_new = x + x_shift  # Add the logic to shift x here
    y_new = y + y_shift  # Add the logic to shift y here

    return x_new, y_new


def check_coincident(a, b):
    """
    Check whether two points are coincident
    Parameters
    ----------
    a : tuple
        A point in the form (x,y)

    b : tuple
        A point in the form (x,y)

    Returns
    -------
    equal : bool
            Whether the points are equal
    """

    if (a[0] == b[0] and a[1] == b[1]):
        equal = True
    else:
        equal = False
    return equal # Add the logic to check if coincident here


def check_in(point, point_list):
    """
    Check whether point is in the point list

    Parameters
    ----------
    point : tuple
            In the form (x,y)

    point_list : list
                 in the form [point, point_1, point_2, ..., point_n]
    """

    return point in point_list # Add the logic to check if a point is in the point list here


def getx(point):
    """
    A simple method to return the x coordinate of
     an tuple in the form(x,y).  We will look at
     sequences in a coming lesson.

    Parameters
    ----------
    point : tuple
            in the form (x,y)

    Returns
    -------
     : int or float
       x coordinate
    """
    return point[0]


def gety(point):
    """
    A simple method to return the x coordinate of
     an tuple in the form(x,y).  We will look at
     sequences in a coming lesson.

    Parameters
    ----------
    point : tuple
            in the form (x,y)

    Returns
    -------
     : int or float
       y coordinate
    """
    return point[1]
