class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        spiral = [[0]*n for i in range(n)]
        x, y, off = 0, 0, 0
        for i in range(1, n*n +1):
            spiral[y][x] = i
            if x == (n-1-off) and y < (n-1-off): y += 1 # Right Edge
            elif y == (n-1-off) and x > off: x -=1 # Bottom Edge
            elif x == off and y > off: # Left Edge
                y -= 1
                if y == off+1: off += 1
            else: x += 1 # Top Edge
        return spiral
