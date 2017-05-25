from nose.tools import assert_equal

class TestCoins(object):

    def check(self,solution):
        coins=[1,5,10,25]
        assert_equal(solution(45,coins,46*[0]),3)
        assert_equal(solution(23,coins,24*[0]),5)
        assert_equal(solution(74,coins,75*[0]),8)
        print("Pass all the tests")

def rec_coin(target,coins,known_results):
    min_coins=target

    if target in coins:
        known_results[target]=1
        return 1

    elif known_results[target]>0:
        return known_results[target]
    else:
        for i in [c for c in coins if c<target]:
            num_coins=1+rec_coin(target-i,coins,known_results)
            if num_coins<min_coins:
                min_coins=num_coins
                known_results[target]=min_coins
    return min_coins

if __name__=="__main__":
    test=TestCoins()
    test.check(rec_coin)
