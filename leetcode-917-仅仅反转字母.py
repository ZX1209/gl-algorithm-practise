# leetcode-917-仅仅反转字母.py
# 给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。

 

# 示例 1：

# 输入："ab-cd"
# 输出："dc-ba"
# 示例 2：

# 输入："a-bC-dEf-ghIj"
# 输出："j-Ih-gfE-dCba"
# 示例 3：

# 输入："Test1ng-Leet=code-Q!"
# 输出："Qedo1ct-eeLg=ntse-T!"


"""
思路:
双指针,,特殊情况
"""

class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        l = len(S)

        if l<=1:
            return S 
        S = list(S)
        left = 0
        right = l-1 

        while left<right:
            while left<right:
                if S[left].isalpha():
                    break
                left += 1

            while left<right:
                if S[right].isalpha():
                    break
                right -=1

            S[left],S[right] = S[right],S[left]
            left+=1
            right-=1

        return "".join(S)






