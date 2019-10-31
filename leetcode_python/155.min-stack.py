#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#
# https://leetcode.com/problems/min-stack/description/
#
# algorithms
# Easy (35.56%)
# Total Accepted:    268.9K
# Total Submissions: 755K
# Testcase Example:  '["MinStack","push","push","push","getMin","pop","top","getMin"]\n[[],[-2],[0],[-3],[],[],[],[]]'
#
# 
# Design a stack that supports push, pop, top, and retrieving the minimum
# element in constant time.
# 
# 
# push(x) -- Push element x onto stack.
# 
# 
# pop() -- Removes the element on top of the stack.
# 
# 
# top() -- Get the top element.
# 
# 
# getMin() -- Retrieve the minimum element in the stack.
# 
# 
# 
# 
# Example:
# 
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.
# 
# 
#
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.my_stack = []
        self.top_index = -1
        self.min_stack = []
        self.min_stack_top = -1
        

    def push(self, x: int) -> None:
        self.top_index += 1
        self.my_stack.append(x)

        if self.min_stack_top == -1 or x <= self.min_stack[self.min_stack_top]:
            self.min_stack_top += 1
            self.min_stack.append(x)
    def pop(self) -> None:
        if self.top_index < 0:
            return None
        pop_val = self.my_stack[self.top_index]
        del(self.my_stack[self.top_index])
        self.top_index -= 1

        if pop_val == self.min_stack[self.min_stack_top]:
            del(self.min_stack[self.min_stack_top])
            self.min_stack_top -= 1

        return pop_val

    def top(self) -> int:
        if self.top_index < 0:
            return None
        return self.my_stack[self.top_index]
        

    def getMin(self) -> int:
        if self.min_stack_top < 0:
            return None
        return self.min_stack[self.min_stack_top]
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

