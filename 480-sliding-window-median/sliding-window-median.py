import bisect
class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        window = sorted(nums[:k])   
        res = []

        for i in range(k, len(nums) + 1):
            if k % 2:
                res.append(float(window[k // 2]))
            else:
                res.append((window[k // 2 - 1] + window[k // 2]) / 2.0)

            if i == len(nums):
                break
            window.remove(nums[i - k])              
            bisect.insort(window, nums[i])          

        return res