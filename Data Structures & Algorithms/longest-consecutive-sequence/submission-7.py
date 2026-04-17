class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)

        # Return 0 if array is empty
        if n == 0:
            return 0 

        nums.sort()

        # Track last smaller element
        lastSmaller = float('-inf') 
        # Count current sequence length
        cnt = 0 
        # Track longest sequence length
        longest = 1 

        for i in range(n):
            # If consecutive number exists
            if nums[i] - 1 == lastSmaller:
                # Increment sequence count
                cnt += 1 
                # Update last smaller element
                lastSmaller = nums[i] 
            # If consecutive number doesn't exist
            elif nums[i] != lastSmaller:
                # Reset count for new sequence
                cnt = 1 
                # Update last smaller element
                lastSmaller = nums[i] 
            # Update longest if needed
            longest = max(longest, cnt) 
        return longest
        