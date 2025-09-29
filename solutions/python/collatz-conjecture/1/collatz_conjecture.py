def steps(number):
    """
    Calculates the number of steps required to reach 1 
    according to the rules of the Collatz Conjecture.

    :param number: A positive integer starting point.
    :returns: The number of steps (int) to reach 1.
    :raises ValueError: If the input 'number' is zero or negative.
    """
    if number <= 0:  # First of all we check if the given number is not 0 or negative. 
      raise ValueError("Only positive integers are allowed")  

    steps = 0

    while number != 1:   # While loop will run until our intiger reaches 1.

        steps += 1

        if number % 2 == 0:
            number = number // 2   # Fist condiotion for even numbers. Use // to return int not float. 
        else:
            number = number * 3 + 1   # Second condition for odd numbers. 
    return steps
    