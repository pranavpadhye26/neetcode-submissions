class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ['+', '-', '*' , '/']:
                val1 = stack.pop()
                val2 = stack.pop()
                if token == '+':
                    res = val1 + val2
                elif token == '-':
                    res = val2 - val1
                elif token == '*':
                    res = val1 * val2
                elif token == '/':
                    res = int(val2/val1)
                stack.append(res)
            else:
                stack.append(int(token))
        return stack[-1]