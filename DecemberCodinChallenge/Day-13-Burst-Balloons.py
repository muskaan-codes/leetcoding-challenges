import numpy as np
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        def getMaxCoins(extended, memoriz, left, right):
            if(left==right):
                return 0
            if(memoriz[left][right]>0):
                return memoriz[left][right];
            max1 = 0
            for i in range(left+1, right):
                max1 = max(max1,extended[left]*extended[i]*extended[right]+getMaxCoins(extended,memoriz,left,i)
                             +getMaxCoins(extended ,memoriz,i,right));

            memoriz[left][right]=max1
            return int(max1)
        
        n=len(nums)
        extended = [0] * (n+2)
        print(extended)
        extended[0] = 1
        extended[n+1] = 1
        for i in range(1, n+1):
            extended[i] = nums[i-1]
        
        memoriz = np.zeros((n+2,n+2))
        return getMaxCoins(extended,memoriz,0,n+1)
