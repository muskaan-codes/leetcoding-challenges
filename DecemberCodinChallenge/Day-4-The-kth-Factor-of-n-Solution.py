class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        factors = lambda n: (f for i in range(1, int(n**0.5)+1) if n % i == 0 for f in [i, n//i])
        facts = []
        for f in factors(n):
            facts.append(f)
        facts = list(set(facts))
        facts.sort()
        return facts[k-1] if len(facts) >= k else -1
                
