#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
# https://leetcode.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (42.74%)
# Total Accepted:    331.5K
# Total Submissions: 769.7K
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# Given n non-negative integers a1, a2, ..., an , where each represents a point
# at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
# of line i is at (i, ai) and (i, 0). Find two lines, which together with
# x-axis forms a container, such that the container contains the most water.
# 
# Note: You may not slant the container and n is at least 2.
# 
# 
# 
# 
# 
# The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In
# this case, the max area of water (blue section) the container can contain is
# 49. 
# 
# 
# 
# Example:
# 
# 
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49
# 
#
class Solution:
    def maxArea(self, height: List[int]) -> int:
        #这种方法效率太低了，在跑性能测试时直接超时了
        '''
        #遍历每一个index的线，从远到近找到比自己高的线求出面积，最后获得最大的
        max_size = 0
        for index in range(len(height)):
            #从左右找到比自己高的线,list分别表示左右线的index和对应的最大面积
            low_index = 0
            high_index = len(height)-1
            #计算左边能得到的最大面积
            while low_index < index:
                if height[low_index] >= height[index]:
                    max_size = max(max_size,height[index]*(index-low_index))
                    break
                low_index += 1
            #计算右边能得到的最大面积
            while high_index > index:
                if height[high_index] >= height[index]:
                    max_size = max(max_size,height[index]*(high_index-index))
                    break
                high_index -= 1
        
        return max_size
        '''
        #从前后往中间靠，找到比之前更高的就计算下装水面积
        water_size = 0
        low_index = 0
        high_index = len(height)-1
        while low_index < high_index:
            cur_height = min(height[low_index],height[high_index])
            water_size = max(water_size,(high_index-low_index)*cur_height)
            while low_index < high_index and height[low_index] <= cur_height:
                low_index += 1
            while high_index > low_index and height[high_index] <= cur_height:
                high_index -= 1
        
        return water_size

            
            

        




