def maxSlidingWindow(self, nums, k):
    
    window = collections.deque()
    
    res = []
    
    for i in range(len(nums)):
        
        if window and i-k >= window[0][1]:           
            window.popleft()
                
        while window and nums[i] > window[-1][0]:
            window.pop()                
        window.append((nums[i], i))
        
        if i >= k - 1:
            res.append(window[0][0])
            
    return res
