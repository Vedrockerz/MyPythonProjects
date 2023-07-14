# -------- FAULTY CALCULATOR ! -------------

def my_function():
    choice = ''' The operations you can perform by respective operators :
             1. Addition by '+'.
             2. Subtraction by '-'.
             3. Multipication by '*'.
             4. Division by '/'.      '''

    print(choice)             
    oper = input("Enter the operator you wants to use: ")
    a = int(input("Enter the first no. : "))
    b = int(input("Enter the second no. : "))

    if oper == "+":
        if a==56 and b==9 or a==9 and b==56:
            print("The sum of entered numbers is : 77")
        else:
            print(f"The sum of entered numbers is : {a+b}")

    elif oper == "-":
        if a==56 and b==9:
            print("The difference of entered numbers is : 38")
        else:
            print(f"The difference of entered numbers is : {a-b}")

    elif oper == "*":
        if a==45 and b==3 or a==3 and b==45:
            print("The product of entered numbers is : 555")
        else:
            print(f"The product of entered numbers is : {a*b}")

    elif oper == "/":
        if a==56 and b==6:
            print("The division of entered numbers is : 4")
        else:
            print(f"The division of entered numbers is : {a/b}")

    else:
        print("Invalid Input or choice")

my_function()

while True:
    print("************* Do you want to do more calculation? *************")
    print("            If yes then write 'y' else 'q' to quit             ")
    userInput = input("Enter your answer : ")
    if userInput.lower() != 'y':
        break
    my_function()



