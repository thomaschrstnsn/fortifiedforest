from Point import Point
from Line import Line
from Path import Path

def allright(line, points):
    """Function to determine if all points are to the right of the given line"""
    right = True
    for p in points:
        if p is line.p1 or p is line.p2: continue # ignore the points in the line
        right = line.angle(p) < 0
        if not right:
            break
    return right

def jarviswalk(points):
    """Implementation of Jarvis Walk aka Gift wrapping algorithm.
    Based on the article http://en.wikipedia.org/wiki/Gift_wrapping_algorithm
    """
    hull = Path()
    xsorted = sorted(points, key=lambda point: point.x)
    hull.addPoint(xsorted[0])
    while True:
        nextP = None
        for p in xsorted:
            line = Line(hull.points[-1], p)
            if allright(line, xsorted):
                nextP = p
                break
        assert(nextP is not None)
        hull.addPoint(nextP) 
        if hull.isConnected():
            break
    return hull
