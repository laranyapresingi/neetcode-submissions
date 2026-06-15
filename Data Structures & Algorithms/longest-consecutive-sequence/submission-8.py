class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       n =len(nums)
       if not nums:
        return 0
       nums.sort()
       cnt = 0
       lastsmall = float('-inf')
       longest = 1

       for i in range(n):
        if nums[i]-1 == lastsmall:
            cnt+=1
            lastsmall = nums[i]
        elif nums[i] != lastsmall:
            cnt=1
            lastsmall = nums[i]
        longest = max(longest,cnt)
    
       return longest