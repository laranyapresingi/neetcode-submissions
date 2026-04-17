from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        e_dict = dict(Counter(nums))
        # print(count_dict)
        e_dict=dict(sorted(e_dict.items(), key=lambda item: item[1], reverse=True))
        last_k_keys =list(e_dict.keys())[:k]
        return last_k_keys
        # n = len(nums)
        # e_dict={}
        # ans=[]
        # for i in range(n):
        #     if nums[i] not in e_dict:
        #         e_dict[nums[i]]=1
        #     else:
        #         e_dict[nums[i]]+=1
        # print(e_dict)
        # e_dict=dict(sorted(e_dict.items(), key=lambda item: item[1], reverse=True))
        # last_k_keys=list(e_dict.keys())[:k]
        # return last_k_keys
