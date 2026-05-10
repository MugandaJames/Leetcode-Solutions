class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        stack = []

        parts = path.split("/")

        for part in parts:

            # ignore empty and current dir
            if part == "" or part == ".":
                continue

            # go to parent
            elif part == "..":

                if stack:
                    stack.pop()

            # valid directory
            else:
                stack.append(part)

        return "/" + "/".join(stack)
