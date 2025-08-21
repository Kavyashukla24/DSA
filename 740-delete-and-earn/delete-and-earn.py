from collections import Counter

class Solution:
    def deleteAndEarn(self, nums):
        count = Counter(nums)
        max_num = max(nums)
    
        prev2, prev1 = 0, count[1] * 1  

        for i in range(2, max_num + 1):
            curr = max(prev1, prev2 + i * count[i])
            prev2, prev1 = prev1, curr

        return prev1