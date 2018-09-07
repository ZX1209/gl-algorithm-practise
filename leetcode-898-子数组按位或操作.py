# leetcode-898-子数组按位或操作.py
# 用户通过次数 0
# 用户尝试次数 0
# 通过次数 0
# 提交次数 0
# 题目难度 Medium
# 我们有一个非负整数数组 A。

# 对于每个（连续的）子数组 B = [A[i], A[i+1], ..., A[j]] （ i <= j），我们对 B 中的每个元素进行按位或操作，获得结果 A[i] | A[i+1] | ... | A[j]。

# 返回可能结果的数量。 （多次出现的结果在最终答案中仅计算一次。）


# 示例 1：

# 输入：[0]
# 输出：1
# 解释：
# 只有一个可能的结果 0 。
# 示例 2：

# 输入：[1,1,2]
# 输出：3
# 解释：
# 可能的子数组为 [1]，[1]，[2]，[1, 1]，[1, 2]，[1, 1, 2]。
# 产生的结果为 1，1，2，1，3，3 。
# 有三个唯一值，所以答案是 3 。
# 示例 3：

# 输入：[1,2,4]
# 输出：6
# 解释：
# 可能的结果是 1，2，3，4，6，以及 7 。


# 提示：

# 1 <= A.length <= 50000
# 0 <= A[i] <= 10^9


"""
消重??有顺序消重...


"""

class Solution:
    def subarrayBitwiseORs(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        l = len(A)
        if l == 1:
            return 1

        i = l-1

        # # 可优化
        # while i > 0:
        #     while A[i-1] == A[i]:
        #         A.pop(i-1)
        #         # 保持 原A[i]
        #         i = i-1
        #         if i <= 0:
        #             break
        #     # 下一个 A[i]
        #     i = i - 1

        l = len(A)

        ans_set = set(A)
        for i in range(2, l+1):
            for j in range(0, l):
                if j+i > l:
                    break
                tmpans = A[j]
                for one in A[j:j+i]:
                    tmpans = tmpans | one
                ans_set.add(tmpans)

        return len(ans_set)


if __name__ == '__main__':
    test = Solution()
    print(test.subarrayBitwiseORs([1, 2, 2, 2, 3, 4, 4, 5]))
