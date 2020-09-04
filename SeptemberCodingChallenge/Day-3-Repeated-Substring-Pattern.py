class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        t = ""
        for x in range(0, len(s) / 2):
            t = t + s[x]
            l = len(t)
            for y in range(l, len(s), l):
                if s[y:(y + l)] == t:
                    if y < len(s) - l:
                        continue
                    else:
                        return True
                else:
                    break
        return False
