def triple_double(num1, num2):
    #code me ^^
    return check_triple(num1)[0]*check_double(num2)[0]*(check_triple(num1)[1] in check_double(num2)[1])


def check_triple(num):
    for i in range(1,len(str(num))-1):
        if str(num)[i-1]==str(num)[i]==str(num)[i+1]:
            return (True,str(num)[i-1])
    return (False,0)

def check_double(num):
    nums=set()
    for i in range(len(str(num))-1):
        if str(num)[i]==str(num)[i+1]:
            nums.append(str(num)[i])
        return (True,nums)
    return (False,1)


print(triple_double(451999277, 41177722899))
# print(check_triple(451999277)[0])
# print(check_double(41177722899)[0])
print(check_triple(451999277)[1])
print(check_double(41177722899)[1])
#print(check_triple(451999277)[1]+" "+check_double(41177722899)[1])
