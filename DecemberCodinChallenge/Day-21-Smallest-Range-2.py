class Solution(object):
    def smallestRangeII(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        ans = A[-1] - A[0]
        for x, y in zip(A, A[1:]):
            ans = min(ans, max(A[-1]-K, x+K) - min(A[0]+K, y-K))
        return ans
