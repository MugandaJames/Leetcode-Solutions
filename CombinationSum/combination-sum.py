class Solution:
    def combinationSum(self, candidates, target):

        result = []

        def backtrack(start, path, total):

            # success case
            if total == target:
                result.append(path[:])
                return

            # failure case
            if total > target:
                return

            for i in range(start, len(candidates)):

                path.append(candidates[i])

                backtrack(i, path, total + candidates[i])

                path.pop()  # undo choice

        backtrack(0, [], 0)

        return result
