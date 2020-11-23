import re
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        groups = s.count('[')
        for _group in range(groups):
            match = re.search(r'(\d*)\[(\w*)\]', s)
            times = int(match.group(1))
            letters = match.group(2)
            s = s.replace(match.group(0), letters*times)
        return s
