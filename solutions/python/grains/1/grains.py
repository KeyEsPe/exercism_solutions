def square(number):
    """
    This function will check first if the number of square 
    is in range from 1 to 64 inclusive. 

    To count numbers of grains on each square:
    number_of_grains = 2 ** number_of_square - 1.
    """
    if number not in range(1, 65):
        raise ValueError("square must be between 1 and 64")
    grains_on_square = 2 ** (number - 1)
    return grains_on_square


def total():
    """
    We use for loop to iterate through each square and sum
    each result to a variable.
    """
    total_grains = 0
    for i in range(1, 65):
        total_grains +=square(i)
    return total_grains
        
        
