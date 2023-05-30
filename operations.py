#Addition
def add(n1, n2):
    return n1 + n2

#subtraction
def substract(n1, n2):
    return n1 - n2

#Multiplication
def multiply(n1, n2):
    return n1 * n2

#Division
def divide(n1, n2):
    return n1 / n2

#Modulos
def modulo(n1, n2):
    return n1 % n2

operation = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
    "%": modulo,
}