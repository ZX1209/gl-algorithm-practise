# leetcode-32-最长有效括号.py
# 题目描述
# 提示帮助
# 提交记录
# 社区讨论
# 阅读解答
# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

# 示例 1:

# 输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"
# 示例 2:

# 输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"



class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        ts = []
        ans = 0
        tmpans  = 0

        for w in s:
            if len(stack)<=0:
                ts.append(w)
                stack.append(w)
            else:
                if w == ')' and stack[-1]=='(':
                    stack.pop()
                    ts.pop()
                    ts.append('c')
                else:
                    ts.append(w)
                    stack.append(w)

        for w in ts:
            if w != 'c':
                tmpans = 0
            else:
                tmpans+=1

            ans = max(tmpans,ans)

        return ans*2

# 参考
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []

        for i,c in enumerate(s):
            if c == ')' and stack and s[stack[-1]] == '(':
                stack.pop()
            else:
                stack.append(i)
        stack.append(len(s))
        max_length = stack[0]

        for index in range(1,len(stack)):
            max_length = max(max_length,stack[index]-stack[index-1]-1)

        return max_length


# 执行用时为 52 ms 的范例
class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 首先利用栈的原理将所有的正确的结果抛去
        # 保存剩下的不能对应的括号
        # 然后统计每个不能对应括号之间的距离的最大值
        temp_list = []
        for i, item in enumerate(s):
            if item == "(":
                temp_list.append(i)
            else:
                if temp_list != [] and s[temp_list[-1]] == "(":
                    temp_list.pop()
                else:
                    temp_list.append(i)
        
        if temp_list == []:
            return len(s)
        longest = 0
        a, b = -1, 0
        for i in temp_list:
            b = i
            longest = max(longest, (b - a - 1))
            a = b
        longest = max(longest, (len(s) - a - 1))
        return longest

if __name__ == '__main__':
    s = "()(())"
    test = Solution()
    r = test.longestValidParentheses(s)
    print(r)



