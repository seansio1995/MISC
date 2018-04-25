def is_valid(brackets):
    openers_to_closers = {
        '(' : ')',
        '{' : '}',
        '[' : ']'
    }
    opens=set(openers_to_closers.keys())
    closes=set(openers_to_closers.values())

    stack=[]
    for char in brackets:
        if char in opens:
            stack.append(char)
        elif char in closes:
            if not stack:
                return False
            else:
                open_match=stack.pop()
                if openers_to_closers[open_match]!=char:
                    return False
    return True


def testCase():
    assert is_valid("{ [ ] ( ) }")==True
    assert is_valid("{ [ ( ] ) }")==False
    assert is_valid("{ [ }")==False

if __name__=="__main__":
    testCase()
