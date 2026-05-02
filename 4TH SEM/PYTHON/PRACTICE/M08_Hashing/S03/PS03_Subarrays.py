# Leetcode Problem 560  
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        result = 0
        prefix_sum = 0
        d = {0: 1}
        
        for num in nums:
            prefix_sum += num
            result += d.get(prefix_sum - k, 0)
            d[prefix_sum] = d.get(prefix_sum, 0) + 1
            
        return result
