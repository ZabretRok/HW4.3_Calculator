number_1=int(input("Please, enter the first number: "))
number_2=int(input("Ok, please enter the second number: "))
operation=input("What do you want to do with these numbers? Insert +, -, * or / to take action!")
if operation== "+":
    print(number_1 + number_2)
elif operation== "-":
    print(number_1 - number_2)
elif operation== "*":
    print(number_1 * number_2)
elif operation== "/":
    print(number_1 / number_2)
else:
    print("This is not a math operation!")

