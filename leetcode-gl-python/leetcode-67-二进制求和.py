# leetcode-67-二进制求和.py
# 题目描述提示帮助提交记录社区讨论阅读解答
# 给定两个二进制字符串，返回他们的和（用二进制表示）。

# 输入为非空字符串且只包含数字 1 和 0。

# 示例 1:

# 输入: a = "11", b = "1"
# 输出: "100"
# 示例 2:

# 输入: a = "1010", b = "1011"
# 输出: "10101"


"""
思路:
是从右往左加啊...

...
...
有无进位

...
....

.....
...


先规整下..

"""


class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        la = len(a)
        lb = len(b)

        a = list("0"+"0"*(lb-la) + a)
        b = "0"+"0"*(la-lb) + b
        l = len(a)
        for i in range(l-1,0,-1):

            if a[i]=='1' and b[i]=='1':
                self.addone(a,i-1)
                a[i]='0'
            elif a[i]=='1' or b[i]=='1':
                a[i] = '1'
            else:
                a[i] = '0'

        if a[0] == "0":
            return "".join(a[1:])
        else:
            return "".join(a)


    def addone(self,s,i):
        while i>=0:
            if s[i]=='1':
                s[i]='0'
            else:
                s[i]='1'
                break

            i -=1

        return s


# 参考
# 执行用时为 40 ms 的范例
# class Solution:
#     def addBinary(self, a, b):
#         """
#         :type a: str
#         :type b: str
#         :rtype: str
#         """
#         return format(int(a,2)+int(b,2),"b")