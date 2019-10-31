#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#
# https://leetcode.com/problems/rotate-array/description/
#
# algorithms
# Easy (28.86%)
# Total Accepted:    267.6K
# Total Submissions: 924.3K
# Testcase Example:  '[1,2,3,4,5,6,7]\n3'
#
# Given an array, rotate the array to the right by k steps, where k is
# non-negative.
# 
# Example 1:
# 
# 
# Input: [1,2,3,4,5,6,7] and k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# 
# 
# Example 2:
# 
# 
# Input: [-1,-100,3,99] and k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
# 
# 
# Note:
# 
# 
# Try to come up as many solutions as you can, there are at least 3 different
# ways to solve this problem.
# Could you do it in-place with O(1) extra space?
# 
#
class Solution:
    def num_reverse(self,nums,start_index,end_index):
        while start_index < end_index:
            temp_num = nums[start_index]
            nums[start_index] = nums[end_index]
            nums[end_index] = temp_num
            start_index += 1
            end_index -= 1
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        #利用额外的内存空间,注意用浅拷贝就行
        if len(nums) == 0:
            return None
        temp_list = nums[:]
        for index in range(len(temp_list)):
            nums[(index+k)%len(temp_list)] = temp_list[index]
        '''
        #不利用额外的内存空间
        list_len,k = len(nums),k%len(nums)
        self.num_reverse(nums,0,list_len-1)
        self.num_reverse(nums,0,k-1)
        self.num_reverse(nums,k,list_len-1)

        

        

