# leetcode-3的幂.py
# 给定一个整数，写一个函数来判断它是否是 3 的幂次方。

# 示例 1:

# 输入: 27
# 输出: true
# 示例 2:

# 输入: 0
# 输出: false
# 示例 3:

# 输入: 9
# 输出: true
# 示例 4:

# 输入: 45
# 输出: false
# 进阶：
# 你能不使用循环或者递归来完成本题吗？

class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False

        if n%10 in {1,3,9,7}:
            while n>1:
                if n % 3 != 0:
                    return False
                n = int(n/3)

            return True
        else:
            return False


# 参考
# 执行用时为 436 ms 的范例
# class Solution:
#     def isPowerOfThree(self, n):
#         """
#         :type n: int
#         :rtype: bool
#         """
#         return n > 0 and 1162261467 % n == 0