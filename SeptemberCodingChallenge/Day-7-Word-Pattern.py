class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        map = {}
        lenPattern = len(pattern)
        words = str.split()
        if lenPattern != len(words):
            return False
        for x in range(0, lenPattern):
            if not map.has_key(pattern[x]):
                map[pattern[x]] = words[x]
        if len(map) != len(set(map.values())):
            return False
        for x in range(0, lenPattern):
            if map[pattern[x]] == words[x]:
                continue
            else:
                return False
        return True
