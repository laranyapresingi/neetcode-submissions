class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicti=defaultdict(list)
        res=[]
        for i in strs:
            s=''.join(sorted(i))
            print(s)
            if s in dicti.keys():
                dicti[s].append(i)
            else:
                dicti[s].append(i)
        for i in dicti.values():
            res.append(i)
        return res

