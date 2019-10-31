#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#
# https://leetcode.com/problems/count-primes/description/
#
# algorithms
# Easy (28.18%)
# Total Accepted:    214.5K
# Total Submissions: 759.2K
# Testcase Example:  '10'
#
# Count the number of prime numbers less than a non-negative number, n.
# 
# Example:
# 
# 
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# 
#
import math
class Solution:
    def isPrime(self,n:int)->bool:
        if n < 2:
            return False
        if n == 2 or n == 3:
            return True
        #除了2的偶数都不是素数
        if n%2 == 0:
            return False
        for i in range(3,int(math.sqrt(n))+1,2):
            if n%i == 0:
                return False
        return True
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        if n <=3:
            return n-2
        prime_cout = 2
        for i in range(4,n):
            if self.isPrime(i):
                prime_cout += 1
        return prime_cout

