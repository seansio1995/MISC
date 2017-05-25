def reverse(n):
    if len(n)<=1:
        return n
    return reverse(n[1:])+n[0]


def testCase():
    assert reverse("string")=="gnirts"
    assert reverse("hell")=="lleh"
    assert reverse("yes")=="sey"


if __name__=="__main__":
    testCase()
