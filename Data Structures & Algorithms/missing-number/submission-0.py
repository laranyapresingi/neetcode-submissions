class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        n_sum=int(n*(n+1)/2)
        arr_sum=0
        for i in range(0,n):
            arr_sum+=nums[i]
        
        return n_sum - arr_sum
