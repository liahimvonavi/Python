from replit import clear
from image import logo

print

def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations= {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}
def calculator():
    print(logo)
    first_number = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        second_number = float(input("What's the next number?: "))
        calculation = operations[operation_symbol]
        answer = calculation(first_number, second_number)
        print(f"{first_number} {operation_symbol} {second_number} = {answer}")
        if input(f"Type 'y' to continue calculating wiht {answer} or 'n' to start again ") =="y":
            first_number=answer
        else:
            should_continue=False
            clear()
            calculator()
calculator()
