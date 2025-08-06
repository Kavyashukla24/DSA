class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i=0
        area=0
        j=len(height)-1
        while(i<j):
            h = min(height[i], height[j])
            area = max(area, h * (j - i))
            
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return area 


        