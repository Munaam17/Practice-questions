class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        
        # Fix the range (start from end, go backwards)
        for i in range(len(s) - 1, -1, -1):
            
            # Skip trailing spaces
            if s[i] == " ":
                if length > 0:   # if we've already started counting, stop
                    break
                continue
            else:
                length += 1
        
        return length

Ob = Solution()
print(Ob.lengthOfLastWord(" Ali is good  "))