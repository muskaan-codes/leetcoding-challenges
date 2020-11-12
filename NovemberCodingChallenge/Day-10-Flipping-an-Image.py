class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        def invertList(l):
            return map(lambda x: x ^ 1, l)
        for i in range(len(A)):
            A[i] = invertList(A[i][::-1])
        return A
        
