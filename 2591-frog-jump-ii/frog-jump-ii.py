class Solution:
    def maxJump(self, stones: List[int]) -> int:
        maxlength=0
        n=len(stones)
        if n==2:
            return (stones[1]-stones[0])

        for i in range(len(stones) - 2):
            maxlength = max(maxlength, stones[i+2] - stones[i])
        return maxlength



        