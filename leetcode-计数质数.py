# leetcode-计数质数.py
# 统计所有小于非负整数 n 的质数的数量。

# 示例:

# 输入: 10
# 输出: 4
# 解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。

"""
这,暴力法??


"""

class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<2:
            return 0
            
        self.note = [0,1]
        
if __name__ == '__main__':
    n = 100
    test = Solution()
    r = test.countPrimes()
    print(r)