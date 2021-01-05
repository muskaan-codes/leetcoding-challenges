class Solution(object):
    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.ans = 0
        def dfs(i, cands):
            if i <= 1:
                self.ans += 1
                return
            for j, x in enumerate(cands):
                if i % x == 0 or x % i == 0:
                    dfs(i-1, cands[:j] + cands[j+1:])
        dfs(n, list(range(1, n+1)))
        return self.ans
        
        
