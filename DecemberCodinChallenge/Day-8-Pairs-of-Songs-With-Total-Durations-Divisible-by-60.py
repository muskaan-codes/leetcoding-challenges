class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        d = {}
        for mins in time:
            key = mins%60
            d[key] = d.setdefault(key, 0) + 1
        result = 0
        for key, value in d.items():
            if key == 0 or key == 30:
                if value >= 2:
                    result += value * (value-1)
            else:
                if 60-key in d:
                    result += value * (d[60-key])
        return result//2
