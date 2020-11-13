#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the A3AJAGBE Password Generator!\n")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


"""
# Order of characters are not randomised

password = ""

for letter in range(1, nr_letters + 1):
  letter_output = random.choice(letters)
  password+=letter_output

for num in range(1, nr_numbers + 1):
  num_output = random.choice(numbers)
  password+=num_output

for symbol in range(1, nr_symbols + 1):
  sym_output = random.choice(symbols)
  password+=sym_output

print(password)
"""

# Order of characters are randomised

password = []

for letter in range(1, nr_letters + 1):
  letter_output = random.choice(letters)
  password+=letter_output

for num in range(1, nr_numbers + 1):
  num_output = random.choice(numbers)
  password+=num_output

for symbol in range(1, nr_symbols + 1):
  sym_output = random.choice(symbols)
  password+=sym_output

random.shuffle(password)

gen_password = ""
for char in password:
  gen_password+=char
print(f"Generated password is: {gen_password}")