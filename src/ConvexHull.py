from Line import Line
from Path import Path

def allrightAndMaxLinearPoint(line, points):
    """Function to determine if all points are to the right of the given line"""
    right = True
    maxLinearDistance = -1.0
    maxLinearPoint = None
    for p in points:
        if p is line.p1 or p is line.p2: continue # ignore the points in the line
        angle = line.angle(p)
        distance = p.distanceTo(line.p1)
        if angle == 0.0 and distance > maxLinearDistance:
            maxLinearPoint = p
            maxLinearDistance = distance
        if right:
            right = angle < 0
    return (right, maxLinearPoint, maxLinearDistance)

def jarviswalk(points):
    """Implementation of Jarvis Walk aka Gift wrapping algorithm.
    Based on the article http://en.wikipedia.org/wiki/Gift_wrapping_algorithm
    """
    hull = Path()
    xsorted = sorted(points, key=lambda point: point.x)
    hull.addPoint(xsorted[0])
    while True:
        nextP = None
        maxLinearPoint = None
        maxLinearDistance = -1.0
        possiblePoints = filter(lambda p: p not in hull.points[1:], xsorted) 
        for p in possiblePoints:
            if p is hull.points[-1]: continue
            line = Line(hull.points[-1], p)
            allright, localMaxLinear, localMaxLinearDistance = allrightAndMaxLinearPoint(line, xsorted)
            if allright:
                nextP = p
                break
            if localMaxLinear is not None and localMaxLinearDistance != -1.0 and localMaxLinearDistance > maxLinearDistance:
                maxLinearPoint, maxLinearDistance = (localMaxLinear, localMaxLinearDistance)
        assert(nextP is not None or (maxLinearPoint is not None and maxLinearDistance > 0.0))
        if nextP is not None:
            hull.addPoint(nextP)
        else:
            hull.addPoint(maxLinearPoint)
        if hull.isConnected():
            break
    return hull
