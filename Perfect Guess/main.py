# ************ THE PERFECT GUESS *****************
try:
    def myGame():
        import random
        randNo = random.randint(1 , 100)
        # print(randNo)
        userGuess = None
        guesses = 0
        userGuess = int(input("Enter your guess between 1 to 100 :\n"))
        guesses += 1
        while(userGuess!=randNo):
            if userGuess == randNo:
                    print("You Guessed it right!")
            else:
                if(userGuess>randNo):
                    userGuess = int(input("You guessed it wrong! Enter smaller no.\n"))
                    guesses += 1
                else:
                    userGuess = int(input("You guessed it wrong! Enter larger no.\n"))
                    guesses += 1

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

except Exception as e:
    print("Invalid input...Error.....")




