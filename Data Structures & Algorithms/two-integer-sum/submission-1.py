class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        hashmap={}
        for i in range(0,n):
            complement = target - nums[i]
            if complement in hashmap:
                return sorted([i,hashmap[complement]])
            
            hashmap[nums[i]] = i
        return []
            