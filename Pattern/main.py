n = int(input("Enter the value of rows you want: "))
choice = input("Enter 0 for False and 1 for True: ")

bool_value = (int(choice))

if bool_value == True:
    for i in range(n):
        print("*" * (i+1))
    

elif bool_value == False:
    for i in range(n):
        print("*" * (n-i))

else:
    print("Invalid Value. Enter either 0 or 1")    





