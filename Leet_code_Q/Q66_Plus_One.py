from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits   # ← YOU MUST STOP HERE
            else:
                digits[i] = 0   # carry continues
        
        return [1] + digits

Ob = Solution()
print(Ob.plusOne([1,8,9]))
print(Ob.plusOne([9,0]))
print(Ob.plusOne([2,9,9]))f
print(Ob.plusOne([2,9,9]))
Ob.plusOne([9,9,9])
