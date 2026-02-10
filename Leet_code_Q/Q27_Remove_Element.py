from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums [i] == val:
                    nums [i], nums [j] = nums [j], nums [i]

        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)      # safer than remove while looping
            else:
                i += 1
        print(nums)

    def removeElement1(self, nums: list[int], val: int) -> int:
        k = 0  # index for placing non-val elements
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
                
        return k, nums[:k]
    
Ob = Solution()
Ob.removeElement([1,0,4,0,9,0,2,1], 0)
print(Ob.removeElement1([2,1,3,0,4,5,2], 2))


