import random
def question():
    answer=int(input("What should the answer be?"))
    if answer==-1:
        answer=random.randrange(1,100)
    guess_num=int(input("How many guesses?"))
    guess_count=0
    guess=0
    while guess_count<guess_num and answer!=guess:
        guess=int(input("Guess a number?"))
        if guess<answer:
            print("The number is lower than that")
        elif guess>answer:
            print("The number is higher than that")
        else:
            print("You win!")
            return
        guess_count+=1
    print("You lose;the number was {}".format(answer))

question()
