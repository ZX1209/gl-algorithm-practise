# leetcode-541-反转字符串 II.py
# 给定一个字符串和一个整数 k，你需要对从字符串开头算起的每个 2k 个字符的前k个字符进行反转。如果剩余少于 k 个字符，则将剩余的所有全部反转。如果有小于 2k 但大于或等于 k 个字符，则反转前 k 个字符，并将剩余的字符保持原样。

# 示例:

# 输入: s = "abcdefg", k = 2
# 输出: "bacdfeg"
# 要求:

# 该字符串只包含小写的英文字母。
# 给定字符串的长度和 k 在[1, 10000]范围内。


"""
思路:
2k 里 的前k个

[k,2k)  前k个

[0,k) 全部
"""

class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        l = len(s)
        s = list(s)

        for i in range(0,l,2*k):
            if l-i>=k:
                if i==0:
                    s[i:i+k] = s[i+k-1::-1]
                else:
                    s[i:i+k] = s[i+k-1:i-1:-1]
            else:
                if i==0:
                    s[i:l] = s[l-1::-1]
                else:
                    s[i:l] = s[l-1:i-1:-1]
        return "".join(s)

if __name__ == '__main__':
    s = "a"
    k = 2
    test = Solution()
    r = test.reverseStr(s,k)
    print(r)



执行用时为 36 ms 的范例
class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        l = len(s)
        res = ''
        for i in range(0, l, 2 * k):
            res += s[i:i + k][::-1] + s[i + k:i + 2 * k]

        return res