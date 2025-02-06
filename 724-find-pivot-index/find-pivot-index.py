class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Step 1: Calculate the total sum of the array
        total_sum = sum(nums)
        
        # Step 2: Initialize the sum of elements to the left of the current index
        left_sum = 0
        
        # Step 3: Iterate through the array using the index
        for i in range(len(nums)):
            # Calculate the sum of elements to the right of the current index
            right_sum = total_sum - left_sum - nums[i]
            
            # Check if the left sum is equal to the right sum
            if right_sum == left_sum:
                # If equal, return the current index as the pivot index
                return i
            
            # Update the left sum by adding the current element
            left_sum += nums[i]
        
        # Step 4: If no pivot index is found, return -1
        return -1

# Example usage:
# Create an instance of the Solution class
solution = Solution()

# Define the input array
nums = [1, 7, 3, 6, 5, 6]

# Call the pivotIndex method and print the result
print(solution.pivotIndex(nums))  # Output: 3