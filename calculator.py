from calc_art import logo

print(logo)


def power(n1, n2):
    return n1 ** n2


def sqrt(n1, n2=0.5):
    return n1 ** n2


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def modulo(n1, n2):
    return n1 % n2


operations = {'+': add,
              '-': subtract,
              '*': multiply,
              '/': divide,
              '%': modulo,
              '^': power,
              'sq': sqrt}


def calculator():
    print("Welcome to the calculator!")
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    cont = True
    while cont:
        operation_symbol = input("Pick an operation: ")
        calculation_function = operations[operation_symbol]
        if calculation_function == sqrt:
            num2 = 0.5
        else:
            num2 = float(input("What's the next number?: "))
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            cont = False
            print("Your final answer is " + str(answer))
    if input("Type 'y' to continue calculating, or type 'n' to exit: ") == 'y':
        calculator()
    else:
        print("Goodbye!")


calculator()
