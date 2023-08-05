# ************ THE PERFECT GUESS *****************

def myGame():
    import random
    randNo = random.randint(1 , 100)
    # print(randNo)
    userGuess = None
    guesses = 0
    while(userGuess!=randNo):
            userGuess = int(input("Enter your guess between 1 to 100 : "))
            guesses += 1 

            if userGuess == randNo:
                print("You Guessed it right!")
            else:
                if(userGuess>randNo):
                    print("You guessed it wrong! a smaller no.")
                else:
                    print("You guessed it wrong! enter a larger no.")

    print(f"You guessed it in {guesses} times")

    with open("Perfect Guess\hiscore_PG.txt" , "r") as f:
        hs = int(f.read())
        
    if (guesses<hs):
        print(f" NEW HIGH SCORE! = {guesses}")
        with open("Perfect Guess\hiscore_PG.txt" , "w") as f:
            f.write(str(guesses))
    else:
        print(f"HIGH SCORE is {hs}")

myGame()

while True:
    print("******* Do you want to check your guess power again? *******")
    print("        If yes then write 'y' else 'q' to quit              ")
    userInput = input("Enter your answer : ")
    if userInput.lower() != 'y':
        break
    myGame()






