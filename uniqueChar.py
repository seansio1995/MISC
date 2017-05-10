def testUnique(s):
    return len(set(s))==len(s)


def testUnique2(s):
    chars=set()
    for letter in s:
        if letter in chars:
            return False
        else:
            chars.add(letter)
    return True

def testCase():
    assert testUnique2("abc")==True
    assert testUnique2("aaabbbc")==False
    assert testUnique("abcd")==True


if __name__=="__main__":
    testCase()
