class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        prevMap = {}
        for i in range(len(numbers)):
            complement = target - numbers[i]
            if complement in prevMap.keys():
                return [prevMap[complement]+1,i+1]
            else:
                prevMap[numbers[i]] = i