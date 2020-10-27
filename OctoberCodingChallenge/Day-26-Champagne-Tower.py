from functools import lru_cache
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        @lru_cache
        def ChampagneFrom(i, j):
            if i < 0:
                return poured
            if j < 0 or j > i:
                return 0
            return max(0, 0.5 * (ChampagneFrom(i-1, j-1) + ChampagneFrom(i-1, j)) - 1)
        return min(1, 0.5 * (ChampagneFrom(query_row-1, query_glass-1) + ChampagneFrom(query_row-1, query_glass)))
