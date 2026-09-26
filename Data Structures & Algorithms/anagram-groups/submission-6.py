from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      ans = defaultdict(list)
      res = []
      for i in strs:
        s = "".join(sorted(i))
        if s in ans.keys():
            ans[s].append(i)
        else:
            ans[s].append(i)
        
      
      for j in ans.values():
        res.append(j)
      
      return res
      


