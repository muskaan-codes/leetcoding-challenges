from itertools import permutations
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or not len(s):
            return 0
        ways = [0 for _ in range(len(s)+1)]
        ways[0] = 1
        ways[1] = 1 if s[0] != '0' else 0
        for i in range(2,len(ways)):
            if 1 <= int(s[i-1]) <= 9:
                ways[i] += ways[i-1]
            if 10 <= int(s[i-2:i]) <= 26:
                ways[i] += ways[i-2]    
        return ways[-1]
