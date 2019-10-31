#
# @lc app=leetcode id=292 lang=python3
#
# [292] Nim Game
#
# https://leetcode.com/problems/nim-game/description/
#
# algorithms
# Easy (55.49%)
# Total Accepted:    178.9K
# Total Submissions: 322.4K
# Testcase Example:  '4'
#
# You are playing the following Nim Game with your friend: There is a heap of
# stones on the table, each time one of you take turns to remove 1 to 3 stones.
# The one who removes the last stone will be the winner. You will take the
# first turn to remove the stones.
# 
# Both of you are very clever and have optimal strategies for the game. Write a
# function to determine whether you can win the game given the number of stones
# in the heap.
# 
# Example:
# 
# 
# Input: 4
# Output: false 
# Explanation: If there are 4 stones in the heap, then you will never win the
# game;
# No matter 1, 2, or 3 stones you remove, the last stone will always
# be 
# removed by your friend.
#
class Solution:
    def canWinNim(self, n: int) -> bool:
        #递归，
        #退出条件，当前个数为1时失败
        #否则只有三种方案，拿走1,2,3个，只要任意一个能赢就行
        #这种方法毫无疑问直接stack溢出了
        '''
        if n <= 3:
            return True
        if n == 4:
            return False
        return self.canWinNim(n-1) or self.canWinNim(n-2) or self.canWinNim(n-3)
        '''
        #想一想，在我拿走后石头剩4个的话我也赢，所以当前n=5,6,7也赢，反之不能让对面拿之前n=5,6，7.所以当前n=8我必输，
        #所以要让对面拿之前n=8，所以当前n=9,10,11我必赢
        #递归下去，会发现n%4 == 0时我输，其他的赢
        return n%4 != 0
        
        
