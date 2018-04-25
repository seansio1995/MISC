def check(number):
    if type(number)!=int or number<=0:
        return False
    digits=[int(d) for d in str(number)]
    digits.reverse()
    sum=0
    for i in range(len(digits)):
        if i%2==0:
            sum+=digits[i]
        if i%2==1:
            double_digit=digits[i]*2
            sum+=(double_digit//10+double_digit%10)
    if sum%10==0:
        return True
    return False
