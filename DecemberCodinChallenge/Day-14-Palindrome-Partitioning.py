class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def isPal(s):
            return s == s[::-1]
        def check(s, path, final):
            if not s:
                final.append(path)
            for i in range(len(s)):
                if isPal(s[:i+1]):
                    check(s[i+1:], path+[s[:i+1]], final)
        op = []
        check(s, [], op)
        return op
