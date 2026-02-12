class Solution(object):
    def generateParenthesis(self, n):
        result = []
        
        def backtrack(path, open_count, close_count):
            # Base case
            if len(path) == 2 * n:
                result.append(path)
                return
            
            # Add '(' if we still have open parentheses left
            if open_count < n:
                backtrack(path + '(', open_count + 1, close_count)
            
            # Add ')' if it won't exceed open parentheses
            if close_count < open_count:
                backtrack(path + ')', open_count, close_count + 1)
        
        backtrack("", 0, 0)
        return result
