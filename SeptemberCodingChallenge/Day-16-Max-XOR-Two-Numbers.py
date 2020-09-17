class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxx = 0
        mask = 0;
        se = set() 
        for i in range(30, -1, -1): 
            mask |= (1 << i) 
            newMaxx = maxx | (1 << i) 
            for n in nums:
                se.add(n & mask)
            for prefix in se:
                if (newMaxx ^ prefix) in se: 
                    maxx = newMaxx 
                    break
            se.clear() 
        return maxx 
