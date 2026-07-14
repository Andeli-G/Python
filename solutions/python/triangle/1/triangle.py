def is_triangle(sides):
    return(sides[0]+sides[1]>=sides[2] and sides[1]+sides[2]>=sides[0] and sides[2]+sides[0]>=sides[1])

def equilateral(sides):
    return(sides[0]==sides[1]==sides[2] and not 0 in sides and is_triangle(sides))
    pass


def isosceles(sides):
    return(len(set(sides))==1 or len(set(sides))==2 and is_triangle(sides))
    pass


def scalene(sides):
    return(len(set(sides))==3 and is_triangle(sides))
    pass
