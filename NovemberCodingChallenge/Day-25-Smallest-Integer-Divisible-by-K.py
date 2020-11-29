class Solution(object):
    def smallestRepunitDivByK(self, K):
        """
        :type K: int
        :rtype: int
        """
        num=0
        for i in range(1,K+1):
            num=(num*10)%K+1
            if(num%K==0):
                return i
        return -1
        
