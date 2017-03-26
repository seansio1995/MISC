def roman():
    number=int(input("Please enter a number:"))
    while number>=1 and number<=3999:
        ints = [1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1]
        nums = ['M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I']
        result=""
        for i in range(len(ints)):
            count=int(number/ints[i])
            result+=count*nums[i]
            number-=count*ints[i]
        print(result)
        return
    print("Input must be between 1 and 3999")


roman()
