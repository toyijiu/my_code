#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#
# https://leetcode.com/problems/merge-sorted-array/description/
#
# algorithms
# Easy (34.79%)
# Total Accepted:    328.4K
# Total Submissions: 943.6K
# Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
#
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as
# one sorted array.
# 
# Note:
# 
# 
# The number of elements initialized in nums1 and nums2 are m and n
# respectively.
# You may assume that nums1 has enough space (size that is greater or equal to
# m + n) to hold additional elements from nums2.
# 
# 
# Example:
# 
# 
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 
# Output: [1,2,2,3,5,6]
# 
# 
#
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #轮询nums2，对每一个val寻找在nums1的插入点
        index_nums1 = 0
        for index_nums2 in range(n):
            #nums1数组的长度也会动态的变化
            while index_nums1 < m + index_nums2:
                if nums2[index_nums2] <= nums1[index_nums1]:
                    nums1.insert(index_nums1,nums2[index_nums2])
                    break
                else:
                    index_nums1 += 1
            #如果该数最大，插入到末尾
            if index_nums1 == m + index_nums2:
                nums1.insert(index_nums1,nums2[index_nums2])
        
        #python数组会自动动态变化，最后需要清除后面的0
        while len(nums1) > m+n:
            del(nums1[len(nums1)-1])


        

