class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = collections.Counter(s)
        stack = []
        added = set()
        for char in s:
            if char not in added:
                while stack and char < stack[-1] and count[stack[-1]] > 0:
                    print(count[stack[-1]])
                    print("Stack %s" % stack)
                    print(added)
                    added.remove(stack.pop())
                stack.append(char)
                added.add(char)
                print("Updated Stack %s" % stack)
                print("updated %s" % added)
            count[char] -= 1
        return ''.join(stack)
