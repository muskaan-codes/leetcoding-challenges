class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        length = len(A)
        if (length < 3):
            return 0
        longestMountain = 0
        current = 0
        while (current < length - 1):
            if (A[current] >= A[current + 1]):
                current += 1
                continue
            mountainStart = current
            while (current < length - 1 and A[current] < A[current + 1]):
                current += 1
            if (current == length - 1):
                break
            while (current < length - 1 and A[current] > A[current + 1]):
                current += 1
            if (current - mountainStart > 1):
                longestMountain = max(current - mountainStart + 1, longestMountain)
        return longestMountain
