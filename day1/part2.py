import re

with open('text1.txt') as f:
    lines = [line.rstrip() for line in f]

# Define the mapping of spelled-out numbers to digits
number_words = {
    "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", 
    "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
}

val = 0

for line in lines:
    # Create a list to store all found digits or spelled-out numbers
    found = []

    # Check each character and the following two characters
    for i in range(len(line)):
        # Extract a substring for potential matching
        substr = line[i:i+5]  # Up to 5 characters, the length of the longest number word

        # Check if the substring matches any spelled-out number
        for word, digit in number_words.items():
            if substr.startswith(word):
                found.append(digit)
                break
        else:
            # If not a word, check if it's a single digit
            if line[i].isdigit():
                found.append(line[i])

    # Extract the first and last 'digit'
    if len(found) >= 2:
        calibration_value = int(found[0] + found[-1])
    elif len(found) == 1:
        calibration_value = int(found[0] * 2)
    else:
        calibration_value = 0
    print(calibration_value)
    val += calibration_value

print(val)
