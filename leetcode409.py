# Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
#
# This is case sensitive, for example "Aa" is not considered a palindrome here.
"""
Input:
"abccccdd"

Output:
7
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        y=list(collections.Counter(s).values())
        length=sum([ch/2 for ch in y])
        length*=2
        length+=bool([ch for ch in y if ch%2==1])
        return length
