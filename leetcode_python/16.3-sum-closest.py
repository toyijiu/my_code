#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest/description/
#
# algorithms
# Medium (40.96%)
# Total Accepted:    298.7K
# Total Submissions: 716.7K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# Given an array nums of n integers and an integer target, find three integers
# in nums such that the sum is closest to target. Return the sum of the three
# integers. You may assume that each input would have exactly one solution.
# 
# Example:
# 
# 
# Given array nums = [-1, 2, 1, -4], and target = 1.
# 
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# 
# 

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        #和15题类似，找出最小的offset值
        if len(nums) < 3:
            return 0
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
    
        for index1 in range(len(nums)-2):
            index2 = index1+1
            index3 = len(nums)-1

            while index2 < index3:
                sum = nums[index1] + nums[index2] + nums[index3]
                if sum == target:
                    return sum
                
                elif abs(sum-target) < abs(result-target):
                    result = sum
                elif sum < target:
                    index2 += 1
                else:
                    index3 -= 1
            
        return result


