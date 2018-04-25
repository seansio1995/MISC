def reverseSentence(s):
    return " ".join(reversed(s.split()))

def reverseSentence2(s):
    return " ".join(s.split()[::-1])


def reverseSentence3(s):
    words=[]
    length=len(s)
    spaces=[" "]

    i=0 #tracker
    while i < length:
        if s[i] not in spaces:
            word_start=i
            while  i<length and s[i] not in spaces :
                i+=1
            words.append(s[word_start:i])
        i+=1
    return " ".join(reversed(words))
def testCase():
    assert reverseSentence('This is the best')=='best the is This'
    assert reverseSentence2('This is the best')=='best the is This'
    assert reverseSentence('  space here')=="here space"
    assert reverseSentence2('space here      ')=="here space"
    assert reverseSentence3('This is the best')=='best the is This'



if __name__=="__main__":
    testCase()
