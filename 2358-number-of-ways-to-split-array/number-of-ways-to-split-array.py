class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total_sum = sum(nums)  # Compute total sum of the array
        prefix_sum = 0  # Initialize prefix sum
        valid_splits = 0
        
        for i in range(len(nums) - 1):  # Iterate through valid split indices
            prefix_sum += nums[i]  # Update prefix sum with the current element
            right_sum = total_sum - prefix_sum  # Calculate right sum
            
            if prefix_sum >= right_sum:  # Check if the split is valid
                valid_splits += 1
        
        return valid_splits