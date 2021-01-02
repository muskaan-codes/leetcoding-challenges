class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        n = len(matrix)
        if n:
            m = len(matrix[0])
        if n == 0 or m == 0:
            return []
        di = [-1, 1]
        dj = [1, -1]
        i, j, d = 0, 0, 0
        ans = []
        while True:
            ans.append(matrix[i][j])
            if i == n - 1 and j == m - 1:
                break
            i, j = i + di[d], j + dj[d]
            if not (0 <= i < n and 0 <= j < m):
                d = 1 - d
                i += 1
                while not (0 <= i < n and 0 <= j < m):
                    i, j = i + di[d], j + dj[d]
        return ans
