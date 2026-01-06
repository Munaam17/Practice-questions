class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        for ch in s:
            # Storing the opening brackets
            if ch == "(" or ch == "{" or ch == "[":
                stack.append(ch)

            else:
                # if stack is empty
                if not stack:
                    return False
                
                # pop the last element to compare
                last = stack.pop()

                if ch == ")" and last != "(":
                    return False
                if ch == "}" and last != "{":
                    return False
                if ch == "]" and last != "[":
                    return False
                
        return len(stack) == 0
    
ob = Solution()
print(ob.isValid("()[{[]()[][]}]"))
print(ob.isValid("()[{[]()[][]]"))
print(ob.isValid("()[{"))
print(ob.isValid("]()[][]}]"))
print(ob.isValid("()[{[][]}]"))
print(ob.isValid("()[{[][]}]"))
print(ob.isValid("()[{[][]}]"))
print(ob.isValid("]()[]{[]}]"))
print(ob.isValid("]()[]{[]}]"))