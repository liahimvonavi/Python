import random
import pass_input
print("Welcome to the PyPassword Generator!")
number_of_letters = int(input("How many letters would you like in your password?\n"))
number_of_symbols = int(input("How many symbols would you like?\n"))
number_of_numbers = int(input("How many numbers would you like?\n"))
password = []


for element in range (0, number_of_letters):
    password += (random.choice(pass_input.letters))
for element in range (0, number_of_symbols):
    password.append (random.choice(pass_input.symbols))
for element in range(0, number_of_numbers):
    password.append(random.choice(pass_input.numbers))

random.shuffle(password)
final_passwd = ''.join(password)
print(f"Here is your password: {final_passwd}")

