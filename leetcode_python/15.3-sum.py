#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (23.46%)
# Total Accepted:    501.2K
# Total Submissions: 2.1M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an array nums of n integers, are there elements a, b, c in nums such
# that a + b + c = 0? Find all unique triplets in the array which gives the sum
# of zero.
# 
# Note:
# 
# The solution set must not contain duplicate triplets.
# 
# Example:
# 
# 
# Given array nums = [-1, 0, 1, 2, -1, -4],
# 
# A solution set is:
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
# 
# 
#
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #这个方法还是效率太低了，倒数第二个用例超时
        '''
        #遍历每次选定一个数nums[i],就变成了找两个数，他们的和是-nums[i]的问题
        #为了避免重复，后两者的起始位置是i+1
        result = []
        num_map = {}
        for index in range(len(nums)):
            for index2 in range(index+1,len(nums)):
                target_num =  -(nums[index]+nums[index2])
                #这个时候不仅要目标值再map中，还要这个值不能和index,index2相同
                if target_num in num_map.keys() and num_map[target_num] != index and num_map[target_num] != index2:
                    temp_list = sorted([nums[index],nums[index2],target_num])
                    if temp_list not in result:
                        result.append(temp_list)
                else:
                    num_map[nums[index2]] = index2
        
        return result
        '''
        #看了下网上的方法，先sort nums,遍历list，取定当前index数，再从右边的list从两边往中间收缩获取剩下的两个数
        nums.sort()
        result = []
        for index1 in range(len(nums)-2):
            if nums[index1] > 0:
                break
            #不加最后一个TC会超时，当前的数字和前一个一样时需要直接跳过
            if index1 > 0 and nums[index1] == nums[index1-1]:
                continue
            index2 = index1 + 1
            index3 = len(nums)-1
            while index2 < index3:
                sum = nums[index1] + nums[index2] + nums[index3]
                if sum > 0:
                    index3 -= 1
                elif sum < 0:
                    index2 += 1
                else:
                    temp_list = [nums[index1],nums[index2],nums[index3]]
                    if temp_list not in result:
                        result.append(temp_list)

                    while index2 < index3 and nums[index2] == nums[index2+1]:
                        index2 += 1
                    while index3 > index2 and nums[index3] == nums[index3-1]:
                        index3 -= 1
                    index2 += 1
                    index3 -= 1
        
        return result


