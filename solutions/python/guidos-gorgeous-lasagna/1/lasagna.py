EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes).

    This function takes an integer representing the elapsed bake time and
    calculates how many additional minutes are needed to reach the
    EXPECTED_BAKE_TIME.
    """
    remaining_bake_time = EXPECTED_BAKE_TIME - elapsed_bake_time
    return remaining_bake_time
   
def preparation_time_in_minutes(number_of_layers):
    """Calculate the total preparation time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :return: int - total preparation time (in minutes).

    This function takes an integer representing the number of layers and
    calculates the total time spent preparing the lasagna based on the
    PREPARATION_TIME per layer.
    """
    preparation_time = number_of_layers * PREPARATION_TIME
    return preparation_time

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
    total_time_in_the_kitchen = preparation_time_in_minutes(number_of_layers)
    return total_time_in_the_kitchen + elapsed_bake_time


