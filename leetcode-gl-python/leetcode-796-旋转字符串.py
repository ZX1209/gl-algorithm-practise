# leetcode-796-旋转字符串.py
# 给定两个字符串, A 和 B。

# A 的旋转操作就是将 A 最左边的字符移动到最右边。 例如, 若 A = 'abcde'，在移动一次之后结果就是'bcdea' 。如果在若干次旋转操作之后，A 能变成B，那么返回True。

# 示例 1:
# 输入: A = 'abcde', B = 'cdeab'
# 输出: true

# 示例 2:
# 输入: A = 'abcde', B = 'abced'
# 输出: false
# 注意：

# A 和 B 长度不超过 100。




class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if A==B:
            return True

        l = len(A)

        for i in range(1,l):
            if A[i:]+A[:i] == B:
                return True
        return False



执行用时为 36 ms 的范例
class Solution:
    def rotateString(self,A, B):
        if A == B:
            return True
        j = 0
        for i in range(1, len(A)+1):
            if (A[i-1:]+A[:i-1]) == B:
                j += 1
        if j == 1:
            return True
        return False
        