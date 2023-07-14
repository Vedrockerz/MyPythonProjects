import datetime
def gettime():
    return datetime.datetime.now()

print("********** HEALTH MANAGEMENT SYSTEM ***********")
print("    #You can keep track of your health here.   ")
print("")
print("What you wants to do --> # Log your data OR Retrieve data" )
print("")

action = int(input("Enter '1' for log data. \n      '2' for retrieve data \n ----->"))
print("")
if action==1 or action==2:
    text1 = '''Our Clients are : i. Ved
                 ii. Rohan
                iii. Piyush   '''
    print(text1 + "\n")
name   = (input("Enter the name of client: "))
print("")
text2 = '''What data do you want to log or retrieve. : 1.Diet plan  OR  2.Exercises'''


def log_data():
    if name.lower() == "ved":
        print(text2 + "\n")
        data = int(input("Enter 1 for Diet plan and 2 for Exercises : "))
        if data == 1:
            with open("python\projects\Health Management System\Ved_diet.txt" , "a") as f:
                value = str(input("Write here : "))
                f.write(f"{str(gettime())} --> {value} \n")
                print("Updated Successfully !")
        elif data == 2:
            with open("python\projects\Health Management System\Ved_exercise.txt" , "a") as f:
                value = str(input("Write here : "))
                f.write(f"{str(gettime())} --> {value} \n")
                print("Updated Successfully !")
        else:
            print("Invalid choice")

    elif name.lower() == "rohan":
        print(text2 + "\n")
        data = int(input("Enter 1 for Diet plan and 2 for Exercises : "))
        if data == 1:
            with open("python\projects\Health Management System\Rohan_diet.txt" , "a") as f:
                value = str(input("Write here : "))
                f.write(f"{str(gettime())} --> {value} \n")
                print("Updated Successfully !")
        elif data == 2:
            with open("python\projects\Health Management System\Rohan_exercise.txt" , "a") as f:
                value = str(input("Write here : "))
                f.write(f"{str(gettime())} --> {value} \n")
                print("Updated Successfully !")
        else:
            print("Invalid choice")

    elif name.lower() == "piyush":
        print(text2 + "\n")
        data = int(input("Enter 1 for Diet plan and 2 for Exercises : "))
        if data == 1:
            with open("python\projects\Health Management System\Piyush_diet.txt" , 'a') as f:
                value = str(input("Write here : "))
                f.write(f"{str(gettime())} --> {value} \n")
                print("Updated Successfully !")
        elif data == 2:
            with open("python\projects\Health Management System\Piyush_exercise.txt" , "a") as f:
                value = str(input("Write here : "))
                f.write(f"{str(gettime())} --> {value} \n")
                print("Updated Successfully !")
        else:
            print("Invalid choice")                    

    else:
        print("Invalid name , 'No client of this name'")

def retrieve_data():
    if name.lower() == "ved":
        print(text2 + "\n")
        data = int(input("Enter 1 for Diet plan and 2 for Exercises : "))
        if data == 1:
            with open("python\projects\Health Management System\Ved_diet.txt" , "r") as f:
                ret = f.read()
                print(ret,end="")
        elif data == 2:
            with open("python\projects\Health Management System\Ved_exercise.txt" , "r") as f:
                ret = f.read()
                print(ret,end="")
        else:
            print("Invalid choice")

    elif name.lower() == "rohan":
        print(text2 + "\n")
        data = int(input("Enter 1 for Diet plan and 2 for Exercises : "))
        if data == 1:
            with open("python\projects\Health Management System\Rohan_diet.txt" , "r") as f:
                ret = f.read()
                print(ret,end="")
        elif data == 2:
            with open("python\projects\Health Management System\Rohan_exercise.txt" , "a") as f:
                ret = f.read()
                print(ret,end="")
        else:
            print("Invalid choice")

    elif name.lower() == "piyush":
        print(text2 + "\n")
        data = int(input("Enter 1 for Diet plan and 2 for Exercises : "))
        if data == 1:
            with open("python\projects\Health Management System\Piyush_diet.txt" , "r") as f:
                ret = f.read()
                print(ret,end="")
        elif data == 2:
            with open("python\projects\Health Management System\Piyush_exercise.txt" , "r") as f:
                ret = f.read()
                print(ret,end="")
        else:
            print("Invalid choice")

    else:
        print("Invalid name , 'No client of this name'")

if action==1:
    log_data()
elif action==2:
    retrieve_data()
else:
    print("Invalid function !")