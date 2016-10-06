# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
#
# For example:
#
# Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.
#
# Follow up:
# Could you do it without any loop/recursion in O(1) runtime?
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        #here we use map
        while num>=10:
            num= sum(list(map(int,str(num))))
        return num


#Alternative solution:
#since sum of digits mod 9, the remainder is always the same

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num>=10:
            if num%9==0:
                return 9
            return num%9
        return num
