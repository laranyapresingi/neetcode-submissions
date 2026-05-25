from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        e_dict = Counter(nums)
        e_dict=dict(sorted(e_dict.items(), key=lambda item: item[1], reverse=True))
        last_k_keys = list(e_dict.keys())[:k]
        return last_k_keys
