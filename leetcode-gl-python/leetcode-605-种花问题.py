# leetcode-605-种花问题.py
# 假设你有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花卉不能种植在相邻的地块上，它们会争夺水源，两者都会死去。

# 给定一个花坛（表示为一个数组包含0和1，其中0表示没种植花，1表示种植了花），和一个数 n 。能否在不打破种植规则的情况下种入 n 朵花？能则返回True，不能则返回False。

# 示例 1:

# 输入: flowerbed = [1,0,0,0,1], n = 1
# 输出: True
# 示例 2:

# 输入: flowerbed = [1,0,0,0,1], n = 2
# 输出: False
# 注意:

# 数组内已种好的花不会违反种植规则。
# 输入的数组长度范围为 [1, 20000]。
# n 是非负整数，且不会超过输入数组的大小。

"""
思路:
算出可能种的区域
"""

class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        def spaceCount(num):
            if num<=2:
                return 0
            else:
                return (num-1)//2

        fstr = "0"+"".join(map(str,flowerbed))+"0"

        fl = fstr.split('1')

        emptyNum = list(map(len,fl))

        return n<=sum(map(spaceCount,emptyNum))


执行用时为 56 ms 的范例
class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        i, length = 0, len(flowerbed)
        while i < length:
            if flowerbed[i] == 0:
                if ((i-1 >= 0 and flowerbed[i-1] == 0) or i == 0) and ((i+1 < length and flowerbed[i+1] == 0) or i == length-1):
                    n -= 1
                    i += 2
                else:
                    i += 1
            else:
                i += 2
            if n <= 0:
                return True 
        return False
        