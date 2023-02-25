import math
def polysum(n, s):
    '''
    n: number of sides of a regular polygon
    s: length of each side
    returns: the sum of the area and square of the perimeter of the polygon, rounded to 4 decimal places
    '''
    area = (0.25 * n * s**2) / (math.tan(math.pi / n))
    perimeter = n * s
    return round(area + perimeter**2, 4)