# Q: Given an integer x, return true if x is a palindrome, and false otherwise.


# Using Loop:

class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = str(x)
        palindrome = a[::-1]

        if (palindrome) == a:
            return True
        else:
            return False

sol = Solution()          # create object
result = sol.isPalindrome(121)
print(result)



# Using Slicing:

class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = str(x)
        palindrome = ""
        for i in range(len(a)-1,-1,-1): #3-1=2, 1, 0
            palindrome += a[i]

        if (palindrome) == a:
            return True
        else:
            return False

sol = Solution()          # create object
result = sol.isPalindrome(121)
print(result)

# Using pure mathematics
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        rev = 0
        while x > rev:
            rev = rev * 10 + x % 10
            x //= 10

        return x == rev or x == rev // 10
    
sol = Solution()          # create object
result = sol.isPalindrome(121)
print(result)