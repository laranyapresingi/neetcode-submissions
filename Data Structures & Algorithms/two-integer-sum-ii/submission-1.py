class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        a=0
        b=n-1
        if n <=1:
            return numbers
        while a < n and b < n:
            if numbers[a] +numbers[b] > target :
                b-=1
            elif numbers[a] +numbers[b] < target:
                a+=1
            else:
                return [a+1,b+1]
        
    