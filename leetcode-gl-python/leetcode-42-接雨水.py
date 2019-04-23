# leetcode-42-接雨水.py
# 题目描述
# 提示帮助
# 提交记录
# 社区讨论
# 阅读解答
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。



# 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

# 示例:

# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6

"""
思路:
左右.
"""
# 参考
class Solution:
    def trap(self, height) -> int:
        highest_right = [0]*len(height)
        for i in range(len(height)-2,-1,-1):
            highest_right[i] = max(highest_right[i+1],height[i+1])
        
        highest_left,depth = [0]*len(height),0
        for i in range(1,len(height)):
            highest_left[i] = max(highest_left[i-1],height[i-1])
            depth += max(0,min(highest_left[i],highest_right[i])-height[i])

        return depth


# 执行用时为 52 ms 的范例
class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxindex=0
        area=0
        movepeak=0
        for i in range(0,len(height)):
            if height[maxindex]<height[i]:
                maxindex=i
        
        for i in range(0,maxindex):
            if movepeak<height[i]:
                movepeak=height[i]
            else:
                area+=movepeak-height[i]
        movepeak=0
        for i in range(len(height)-1,maxindex,-1):
            if movepeak<height[i]:
                movepeak=height[i]
            else:
                area+=movepeak-height[i]
        return area
        
 