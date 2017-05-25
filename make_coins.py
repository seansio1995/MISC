def make_coins(target,coins):
    min_coins=target ##weird>?????

    if target in coins:
        return 1
    else:

        for i in [c for c in coins if c<target]:
            num_coins=1+make_coins(target-i,coins)

            if num_coins<min_coins:
                min_coins=num_coins
    return min_coins


def testCase():
    assert make_coins(63,[1,5,10,25])==6


if __name__=="__main__":
    testCase()

######SLOW
