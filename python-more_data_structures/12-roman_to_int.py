#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    else:
        roman_values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        total = 0
        prev_val = 0

        for char in reversed(roman_string):
            value = roman_values.get(char, 0)  # Collect values of each char
            # If current value < previous value, it's a substraction in Roman
            if value < prev_val:
                total -= value
            else:
                total += value

            prev_val = value

        return total
