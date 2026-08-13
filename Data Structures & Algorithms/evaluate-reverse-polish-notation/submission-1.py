class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for t in tokens:
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "-":
                r = stack.pop()
                l = stack.pop()
                stack.append(l - r)
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            elif t == "/":
                r = stack.pop()
                l = stack.pop()
                stack.append(int(float(l) / r))
            else:
                stack.append(int(t))
        return stack.pop()