class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        q = collections.deque()
        q.append(start)
        visited = set()
        while q:
            cur_i = q.popleft()
            if arr[cur_i] == 0:
                return True
            a, b = cur_i + arr[cur_i], cur_i - arr[cur_i]
            if a < len(arr) and a not in visited:
                q.append(a)
                visited.add(a)
            if b >= 0 and b not in visited:
                q.append(b)
                visited.add(b)
        return False
