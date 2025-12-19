class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        ans = 0

        for i in range(len(s)):
            curr = roman[s[i]]
            ans += curr
            # subtract if previous numeral is smaller
            if i > 0 and roman[s[i-1]] < curr:
                ans -= 2 * roman[s[i-1]]

        return ans
    
sol = Solution()
print(sol.romanToInt("XM"))      # 9
print(sol.romanToInt("XL"))      # 40
print(sol.romanToInt("MCMXCIV")) # 1994
