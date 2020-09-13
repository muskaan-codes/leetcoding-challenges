class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        from itertools import combinations
        perm = combinations([1, 2, 3, 4, 5, 6, 7, 8, 9], k)
        l = list(perm)
        returnList = []
        for x in l:
            if sum(x) == n:
                returnList.append(x)
        return returnList
        
