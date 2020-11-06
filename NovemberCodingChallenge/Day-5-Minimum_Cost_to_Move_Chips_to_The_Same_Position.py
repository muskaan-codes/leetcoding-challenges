class Solution(object):
    def minCostToMoveChips(self, position):
        """
        :type position: List[int]
        :rtype: i
        """
        e = 0
        o = 0
        for x in position:
            if x % 2 == 0:
                e += 1
            else: 
                o += 1
        return min(e,o)
                
