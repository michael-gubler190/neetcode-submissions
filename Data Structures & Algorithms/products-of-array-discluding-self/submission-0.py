class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            current_num = nums[i]
            result[i] = prefix
            prefix *= current_num
        

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            current_num = nums[i]
            result[i] *= postfix
            postfix *= current_num
        
        return result