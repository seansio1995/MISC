def triple_double2(num1,num2):
    num1=str(num1)
    num2=str(num2)
    nums=[]
    for i in range(len(num2)-1):
        if num2[i]==num2[i+1]:
            nums.append(num2[i])
    if len(nums)==0:
        return 0
    for j in range(len(num1)-1):
        if num1[j] in nums and num1[j-1]==num1[j]==num1[j+1]:
            return 1
    return 0

print(triple_double2(451999277, 41177722899))
