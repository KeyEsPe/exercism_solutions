def convert(number):
    """
    We will create an empty string first to store each sound. 
    Thank we have to check each condition separetely and add sound to our string.
    If no condition was fullfiled, our sound string will remain empty - 
    than we can return string from the number provided by converting it. 
    """
    sound = ""
    
    if number % 3 == 0:
        sound = sound + "Pling"
    if number % 5 == 0:
        sound = sound + "Plang"
    if number % 7 == 0:
        sound = sound + "Plong"
    if len(sound) == 0:
        return str(number)
    return sound 
