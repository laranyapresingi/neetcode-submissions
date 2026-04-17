class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums2 = sorted(nums)
        n = len(nums2)
        s =set(nums2)
        ans = []
        for i in range(1,n+1):
            print(i)
            if i not in nums2:
                ans.append(i)
        
        return ans