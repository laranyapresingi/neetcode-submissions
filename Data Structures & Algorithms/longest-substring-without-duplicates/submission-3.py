class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # charset = set()
        # l=0
        # res=0

        # for r in range(len(s)):
        #     while s[r] in charset:
        #         charset.remove(s[l])
        #         l+=1
        #     charset.add(s[r])
        #     res= max(res,r-l+1)
        # return res
        char_set = set()
        left=0
        res=0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left+=1
            
            char_set.add(s[right])
            res = max(res,right-left+1)
        return res

