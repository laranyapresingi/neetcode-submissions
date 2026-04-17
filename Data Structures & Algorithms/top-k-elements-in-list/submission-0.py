from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic=Counter(nums)
        ans=[]
        # print(dic)
        freq=[[] for _ in range(len(nums)+1)]
        for i,count in dic.items():
            freq[count].append(i)
        print(freq)
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                ans.append(num)
                if len(ans)==k:
                    return ans


        