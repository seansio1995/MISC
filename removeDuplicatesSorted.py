def removeDuplicates(listinput):
    i=0
    j=0
    while i<len(listinput)-1:
        res[j]=listinput[i]
        if listinput[i]==listinput[i+1]:
            i+=1
        i+=1
        j+=1
