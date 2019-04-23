# leetcode-791-自定义字符串排序.py
# 题目描述
# 提示帮助
# 提交记录
# 社区讨论
# 阅读解答
# 字符串S和 T 只包含小写字符。在S中，所有字符只会出现一次。

# S 已经根据某种规则进行了排序。我们要根据S中的字符顺序对T进行排序。更具体地说，如果S中x在y之前出现，那么返回的字符串中x也应出现在y之前。

# 返回任意一种符合条件的字符串T。

# 示例:
# 输入:
# S = "cba"
# T = "abcd"
# 输出: "cbad"
# 解释: 
# S中出现了字符 "a", "b", "c", 所以 "a", "b", "c" 的顺序应该是 "c", "b", "a". 
# 由于 "d" 没有在S中出现, 它可以放在T的任意位置. "dcba", "cdba", "cbda" 都是合法的输出。
# 注意:

# S的最大长度为26，其中没有重复的字符。
# T的最大长度为200。
# S和T只包含小写字符。


"""
思路:
根据s中的字符顺序对T进行排序

从后往前..逐步
"""

class Solution:
    def customSortString(self, S: str, T: str) -> str:
        T = list(T)
        ans = []

        for sw in S:
            for i in range(len(T)):
                if T[i] == sw:
                    ans.append(sw)
                    T[i] = ''

        return "".join(ans)+"".join(T)



# 执行用时为 40 ms 的范例
class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        order_dict = {}
        len_dict = {}
      
        result_S = ''
        result_not = ''
        for i in range(len(S)):
            order_dict[i] = S[i]
            len_dict[S[i]] = 0

        for i in range(len(T)):
            if T[i] in len_dict.keys():
                len_dict[T[i]] += 1
            else:
                result_not += T[i]

        for i in range(len(S)):
            result_S += (order_dict[i] * len_dict[order_dict[i]])

        return result_S + result_not