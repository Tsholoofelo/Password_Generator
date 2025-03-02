
import random
import string

# Defining characters
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

print("Welcome to Password Generator!")

# User input
n_letters = int(input("How many letters do you want in your password?\n"))
n_symbols = int(input("How many symbols do you want in your password?\n"))
n_numbers = int(input("How many numbers do you want in your password?\n"))

password_list = []  # List to store password characters

# Adding random letters
for _ in range(n_letters):
    password_list.append(random.choice(letters))

# Adding random symbols
for _ in range(n_symbols):
    password_list.append(random.choice(symbols))

# Adding random numbers
for _ in range(n_numbers):
    password_list.append(random.choice(numbers))

# Shuffling the password list
random.shuffle(password_list)

# Converting list to string
password = "".join(password_list)
#Output
print("Your generated Password is:", password)
