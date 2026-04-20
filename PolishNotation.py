# Time Complexity : O(n)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
# Approach : We go through each token in the expression one by one.
# If it’s a number, we just push it; if it’s an operator, we pop two numbers and compute.
# The final answer is the last value left in the stack.

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ('+', '-', '*', '/')

        for token in tokens:
            if token in operators:
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(self.operation(op2, op1, token))
            else:
                stack.append(int(token))

        return stack.pop()

    def operation(self, op1, op2, op):
        if op == '+':
            return op1 + op2
        elif op == '-':
            return op1 - op2
        elif op == '*':
            return op1 * op2
        elif op == '/':
            return int(op1 / op2)
    