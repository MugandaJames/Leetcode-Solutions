class Solution(object):
    def isValid(self, s):
        stack = []
        
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        for char in s:
            # If it's a closing bracket
            if char in mapping:
                # If stack empty → invalid
                if not stack:
                    return False
                
                top = stack.pop()
                
                # If not matching pair
                if mapping[char] != top:
                    return False
            else:
                # Opening bracket
                stack.append(char)
        
        # If stack empty → valid
        return len(stack) == 0
