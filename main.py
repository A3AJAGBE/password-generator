"""
An application that generates a strong password of varying length that include letters, numbers and symbols
"""
from logo import logo, letters, numbers, symbols
import random

# Default Display
print(logo)
print('Generate a strong password that includes letters, numbers and symbols\n')

# Inputs
password_length = int(input("What is your required password length?\n"))

# Generating the password
password = []
if password_length <= 5:
    for num in range(1):
        num_output = random.choice(numbers)
        password += num_output
        password_length -= len(num_output)

    for symbol in range(1):
        symbol_output = random.choice(symbols)
        password += symbol_output
        password_length -= len(symbol_output)

    for letter in range(password_length):
        letter_output = random.choice(letters)
        password += letter_output
else:
    for num in range(2, 4):
        num_output = random.choice(numbers)
        password += num_output
        password_length -= len(num_output)

    for symbol in range(2, 4):
        symbol_output = random.choice(symbols)
        password += symbol_output
        password_length -= len(num_output)

    for letter in range(password_length):
        letter_output = random.choice(letters)
        password += letter_output

# Shuffle the generated password
random.shuffle(password)

# Convert the list to string
password_generated = ""
for char in password:
    password_generated += char
print(f"Generated password is: {password_generated}")
print('Thank you for using this application!')
