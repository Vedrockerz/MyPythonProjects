# Playing by multiplyers:
import random
try:
    def guess_Game(a,b,actual):
        trials = 1
        user_Guess = int(input(f"Enter the guess number between {a} and {b}\n"))
        while actual != user_Guess :
            if actual > user_Guess:
                user_Guess = int(input(f"Enter the larger number\n"))
                trials+=1
            else : 
                user_Guess = int(input(f"Enter the smaller number\n"))
                trials+=1

        print(f"Congrats! You guessed it in {trials}")
        return trials

    if __name__ == '__main__' :
        a = int(input("Enter the value of a\n"))
        b = int(input("Enter the value of b\n"))

        actual1 = random.randint(a,b)
        print("***** Player 1's Turn *****\n")
        p1 = guess_Game(a,b,actual1)
        
        actual2 = random.randint(a,b)
        print("***** Player 2's Turn *****\n")
        p2 = guess_Game(a,b,actual2)

        if p1<p2 : 
            print("Player 1 wins..!")
        elif p2<p1 : 
            print("Player 2 wins..!")
        else : 
            print("Match Tie..!")

        print(f"Player 1's number is {actual1} and Player 2's number is {actual2} ")
except Exception as e:
    print("------  ERROR  --------")