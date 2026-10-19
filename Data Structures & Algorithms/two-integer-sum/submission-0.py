class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()

        for i in range(len(nums)):
            current_num = nums[i]
            difference = target - current_num

            if difference in seen:
                return [seen[difference], i]
            
            seen[current_num] = i
        
        return [-1, -1]
