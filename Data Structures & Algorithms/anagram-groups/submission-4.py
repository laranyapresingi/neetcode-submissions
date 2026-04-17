class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        prevMap=defaultdict(list)
        ans=[]
        for i in strs:
            a = ''.join(sorted(i))
            if a in prevMap:
                prevMap[a].append(i)
            else:
                prevMap[a].append(i)
        for j in prevMap.values():
            ans.append(j)
        return ans
