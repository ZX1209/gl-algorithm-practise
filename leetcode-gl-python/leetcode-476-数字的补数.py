# leetcode-476-数字的补数.py
# 给定一个正整数，输出它的补数。补数是对该数的二进制表示取反。

# 注意:

# 给定的整数保证在32位带符号整数的范围内。
# 你可以假定二进制数不包含前导零位。
# 示例 1:

# 输入: 5
# 输出: 2
# 解释: 5的二进制表示为101（没有前导零位），其补数为010。所以你需要输出2。
# 示例 2:

# 输入: 1
# 输出: 0
# 解释: 1的二进制表示为1（没有前导零位），其补数为0。所以你需要输出0。

"""
思路:
这,可以直接找到最近的二进制阶位然后减吧,要减一吗?

嗯,对数运算..
"""

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        j = 1

        while 2**j<=num:
            j+=1

        return (2**j)-1-num


执行用时为 20 ms 的范例
import math
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        x = math.floor(math.log(num, 2)) + 1
        return int(2**x) - num - 1