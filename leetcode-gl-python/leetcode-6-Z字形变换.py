# leetcode-6-Z字形变换.py
# 将字符串 "PAYPALISHIRING" 以Z字形排列成给定的行数：

# P   A   H   N
# A P L S I I G
# Y   I   R
# 之后从左往右，逐行读取字符："PAHNAPLSIIGYIR"

# 实现一个将字符串进行指定行数变换的函数:

# string convert(string s, int numRows);
# 示例 1:

# 输入: s = "PAYPALISHIRING", numRows = 3
# 输出: "PAHNAPLSIIGYIR"
# 示例 2:

# 输入: s = "PAYPALISHIRING", numRows = 4
# 输出: "PINALSIGYAHRPI"
# 解释:

# P     I    N
# A   L S  I G
# Y A   H R
# P     I


"""
思路:
搞个数组排?

找规律

范例是找间距,,上边和下边都好找
中间的要全减两边,,算是吧
"""


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows<=1:
            return s
        rows = [[] for _ in range(numRows)]

        i = 0
        l = len(s)
        if i<l:rows[0].append(s[i])
        i+=1

        while i<l:
            for tmpi in range(1,numRows):
                if i<l:rows[tmpi].append(s[i])
                i+=1

            for tmpi in range(numRows-2,-1,-1):
                if i<l:rows[tmpi].append(s[i])
                i+=1

        return "".join(["".join(tmps) for tmps in rows])

# 执行用时为 84ms 的范例
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1: return s
        ans = ""
        interval = 2 * (numRows - 1)
        for i in range(0, len(s), interval):
            ans += s[i]
        for row in range(1, numRows - 1):
            inter = 2 * row
            i = row
            while i < len(s):
                ans += s[i]
                inter = interval - inter
                i += inter
        print(ans)
        for i in range(numRows - 1, len(s), interval):
            ans += s[i]
        return ans
            