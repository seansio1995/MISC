def balanceCheck(s):
    if len(s)%2!=0:
        return False

    opening=set('{([')
    matches = set([ ('(',')'), ('[',']'), ('{','}') ])


    stack=[]

    for paren in s:
        if paren in opening:
            stack.append(paren)
        else:
            if len(stack)==0:
                return False

            last_open=stack.pop()
            if (last_open,paren) not in matches:
                return False
    return len(stack)==0


def testCase():
    assert balanceCheck('[](){([[[]]])}(')==False
    assert balanceCheck('[{{{(())}}}]((()))')==True
    assert balanceCheck('[[[]])]')==False

if __name__=="__main__":
    testCase()
