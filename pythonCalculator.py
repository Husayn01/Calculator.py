from operations import add, substract, multiply, divide, operation
import pyfiglet

calculatorArt = pyfiglet.figlet_format("Calculator")
print(calculatorArt)

def calculator():
    num1 = int(input("Enter a number: "))
    print("---------------------------------------")
    print("+ - * / %")
    print("---------------------------------------")
    pickOperator = input("Pick an operation from the line above: ")
    print("---------------------------------------")
    num2 = int(input("Enter another number: "))
    print("---------------------------------------")
    if pickOperator not in operation:
        print(f"{pickOperator} is an invalid or unsupported  operator")
    else:
        functionCalc = operation[pickOperator]
        firstAnswer = functionCalc(num1, num2)
        print(f"{num1} {pickOperator} {num2} = {firstAnswer}")
    print("---------------------------------------")

    runAgain = True
    while runAgain == True:
        inputContinue = input('''
        Type 'y' to continue calculating with the result. 
        Type 'n' to exit  
        Type 's' to start again:\n ''').lower()
        print("---------------------------------------")

        if inputContinue == "y":           
            pickOperator = input("Pick another operation: ")
            print("---------------------------------------")
            num3 = int(input("pick another number: "))
            print("---------------------------------------")
            functionCalc = operation[pickOperator]
            secondAnswer = functionCalc(firstAnswer, num3)
            print(f"{firstAnswer} {pickOperator} {num3} = {secondAnswer}")

        elif inputContinue == "n":
            runAgain = False
            print("Exited successfully")
            print("---------------------------------------")

        elif inputContinue == "s":
            runAgain = False
            calculator()

        else:
            print("Invalid command")
calculator()