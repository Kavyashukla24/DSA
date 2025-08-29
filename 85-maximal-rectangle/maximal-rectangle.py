class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix: 
            return 0
        
        n = len(matrix[0])
        heights = [0] * n
        max_area = 0

        for row in matrix:
            # Update histogram heights
            for j in range(n):
                if row[j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0
            
            # Compute max rectangle in histogram for this row
            max_area = max(max_area, self.largestRectangleArea(heights))
        
        return max_area

    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        heights.append(0)  # sentinel to clear stack at the end
        
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        
        heights.pop()
        return max_area
