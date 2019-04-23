# leetcode-836-矩形重叠.py
# 矩形以列表 [x1, y1, x2, y2] 的形式表示，其中 (x1, y1) 为左下角的坐标，(x2, y2) 是右上角的坐标。

# 如果相交的面积为正，则称两矩形重叠。需要明确的是，只在角或边接触的两个矩形不构成重叠。

# 给出两个矩形，判断它们是否重叠并返回结果。

# 示例 1：

# 输入：rec1 = [0,0,2,2], rec2 = [1,1,3,3]
# 输出：true
# 示例 2：

# 输入：rec1 = [0,0,1,1], rec2 = [1,0,2,1]
# 输出：false
# 说明：

# 两个矩形 rec1 和 rec2 都以含有四个整数的列表的形式给出。
# 矩形中的所有坐标都处于 -10^9 和 10^9 之间。



class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        if rec2[1]>=rec1[3] or rec2[3]<=rec1[1] or rec2[0]>= rec1[2] or rec2[2]<=rec1[0]:
            return False
        return True


执行用时为 36 ms 的范例
class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        blX1, blY1, trX1, trY1 = rec1
        blX2, blY2, trX2, trY2 = rec2
        
        return ((blX1 < trX2) and (blX2 < trX1)) and \
                ((blY1 < trY2) and (blY2 < trY1))