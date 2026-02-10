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


Ob = Solution()
Ob.removeElement([2,1,3,0,4,5,2], 2)

