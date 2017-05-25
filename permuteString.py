def permute(s):
    out=[]
    if len(s)==1:
        out=[s]
    else:
        for i, let in enumerate(s):
            for perm in permute(s[:i]+s[i+1:]):
                out+=[let+perm]

    return out


def testCase():
    assert sorted(permute('abc'))==sorted(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    assert sorted(permute("dog"))==sorted(['dog', 'dgo', 'odg', 'ogd', 'gdo', 'god'])

if __name__=="__main__":
    testCase()
