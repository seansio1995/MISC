class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        #edge case:
        if num < 0:
            return False
        for factor in [2,3,5]:

            while num % factor==0:
                num/=factor
        print(num)
        return num==1


if __name__=="__main__":
    num=8
    a=Solution()
    print(a.isUgly(num))
