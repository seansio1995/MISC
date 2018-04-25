# a=[1,2,3,4,1]
# d={}
# for i,j in enumerate(a):
#     d[j]=i
# print(d)
# print(min(d.keys()))
import collections
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        d1={}
        d2={}

        for i,j in enumerate(list1):
            d1[j]=i

        for i,j in enumerate(list2):
            d2[j]=i

        d=collections.defaultdict(list)
        commons=list(set(d2) & set(d1))

        for r in commons:
            d[d1[r]+d2[r]].append(r)

        res=d[min(d.keys())]
        return res
