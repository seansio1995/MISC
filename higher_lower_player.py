def guess():
    print("Think of a number between 1 and 100, and I will guess it")
    guess_num=int(input("How many guesses do I have?"))
    count=0
    start=1
    end=100
    middle=(start+end)//2
    while count<guess_num:
        if (end-start) <=1:
            print("Wait; How can it be both higher than {} and lower than {}?".format(start,end))
            return
        flag=input("Is the number higher,lower or same as {}? ".format(middle))
        if flag=="lower":
            end=middle
        if flag=="higher":
            start=middle
        if flag=="same":
            print("You guess it correctly!")
            break
        middle=(start+end)//2
        count+=1
    answer=int(input("I lost; What was the answer"))
    print("Well played!")

guess()
