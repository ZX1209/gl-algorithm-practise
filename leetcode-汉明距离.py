# leetcode-汉明距离.py
# 两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。

# 给出两个整数 x 和 y，计算它们之间的汉明距离。

# 注意：
# 0 ≤ x, y < 231.

# 示例:

# 输入: x = 1, y = 4

# 输出: 2

# 解释:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑

# 上面的箭头指出了对应二进制位不同的位置。


"""
思路:
可以直接遍历求解

同或

count 与 replace...
"""

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        return len(bin(x^y).replace('0',''))-1


# 参考
# 执行用时为 24 ms 的范例
# class Solution(object):
#     def hammingDistance(self, x, y):
#         """
#         :type x: int
#         :type y: int
#         :rtype: int
#         """
#         return  bin(x^y).count('1')