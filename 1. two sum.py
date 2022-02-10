

nums = [2,7,11,15]
target = 9
wynik=[]

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i, j in nums:
            if i == target - j:
                return wynik[(nums.index[i]), (nums.index[j])]             
            else:
                return     
print(nums)
print(wynik)