class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counts = dict()
        buckets = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            num_counts[num] = num_counts.get(num, 0) + 1
        
        for num in num_counts:
            num_count = num_counts[num]
            buckets[num_count].append(num)

        result = []
        i = len(buckets) - 1

        while i >= 0 and len(result) != k:
            bucket = buckets[i]
            for num in bucket:
                result.append(num)
            
            i -= 1
        
        return result