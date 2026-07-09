def square(number):
    """Determines the number of grain on a specific square"""
    if number <= 0 or number> 64:
        raise ValueError('square must be between 1 and 64')
     
    return(2**(number-1))
    pass


def total():
    "Determines the number of grains on the table"
    return(sum([square(i) for i in range(1,65)]))
    pass
