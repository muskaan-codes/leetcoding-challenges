class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        for x in s:
            t = t.replace(x, '', 1)
        return t
