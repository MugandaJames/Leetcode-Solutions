class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        stack = []

        for t in tokens:

            if t in "+-*/":

                b = stack.pop()
                a = stack.pop()

                if t == "+":
                    stack.append(a + b)
                elif t == "-":
                    stack.append(a - b)
                elif t == "*":
                    stack.append(a * b)
                else:
                    # important: truncate toward zero
                    stack.append(int(a / float(b)))

            else:
                stack.append(int(t))

        return stack[0]
