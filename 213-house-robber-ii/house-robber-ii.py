class Solution:
    def rob(self, nums):
        def rob_linear(houses):
            prev = curr = 0
            for num in houses:
                prev, curr = curr, max(curr, prev + num)
            return curr

        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        case1 = rob_linear(nums[:-1])
        case2 = rob_linear(nums[1:])

        return max(case1, case2)
