def is_armstrong_number(number):
    string = str(number)
    power = len(string)
    total_sum = 0

    for digit_string in string:
        digit = int(digit_string)
        total_sum += digit ** power

    return total_sum == number
        