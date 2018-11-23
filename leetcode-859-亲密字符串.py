# leetcode-859-亲密字符串.py
# 给定两个由小写字母构成的字符串 A 和 B ，只要我们可以通过交换 A 中的两个字母得到与 B 相等的结果，就返回 true ；否则返回 false 。

 

# 示例 1：

# 输入： A = "ab", B = "ba"
# 输出： true
# 示例 2：

# 输入： A = "ab", B = "ab"
# 输出： false
# 示例 3:

# 输入： A = "aa", B = "aa"
# 输出： true
# 示例 4：

# 输入： A = "aaaaaaabc", B = "aaaaaaacb"
# 输出： true
# 示例 5：

# 输入： A = "", B = "aa"
# 输出： false
 

# 提示：

# 0 <= A.length <= 20000
# 0 <= B.length <= 20000
# A 和 B 仅由小写字母构成。

"""
思路:
双指针?
"""

class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """

        if len(A)!=len(B):
            return False

        if A==B:
            return False

        l = len(A)

        left = 0
        right = l-1

        hasSame = 0

        while left<right:
            if A[left]!=B[left]:
                break
            left+=1

        while left<right:
            if A[right]!=B[right]:
                break
            right-=1

        if left<l:
            # problem
            A = list(A)
            A[left] ,A[right] = A[right],A[left]
            A = "".join(A)
            return A==B
        else:
            return len(set(A))<len(A)


        # if len(A)!=len(B):
        #     return False

        # if A==B:
        #     return False

        # l = len(A)

        # left = 0
        # right = l-1

        # ismodified = 0

        # while left<right:
        #     while left<right:
        #         if A[left]!=B[left]:
        #             break
        #         left+=1

        #     while left<right:
        #         if A[right]!=B[right]:
        #             break
        #         right-=1

        #     if left<right and ismodified:
        #         return False

        #     if A[left] == B[right] and A[right] == B[left]:
        #         ismodified = 1
        #         left+=1
        #         right-=1
        #     else:
        #         return False

        # return bool(ismodified)


# 参考
class Solution(object):
    def buddyStrings(self, A, B):
        if len(A) != len(B): return False
        if A == B:
            seen = set()
            for a in A:
                if a in seen:
                    return True
                seen.add(a)
            return False
        else:
            pairs = []
            for a, b in itertools.izip(A, B):
                if a != b:
                    pairs.append((a, b))
                if len(pairs) >= 3: return False
            return len(pairs) == 2 and pairs[0] == pairs[1][::-1]