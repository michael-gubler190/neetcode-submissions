class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        pointer1 = 0
        pointer2 = len(heights) - 1

        while pointer1 < pointer2:
            left_height = heights[pointer1]
            right_height = heights[pointer2]

            lower_height = min(left_height, right_height)

            current_area = lower_height * (pointer2 - pointer1)
            if current_area > max_area:
                max_area = current_area
            
            if lower_height == left_height:
                pointer1 += 1
            else:
                pointer2 -= 1
        
        return max_area