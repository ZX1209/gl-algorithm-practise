# leetcode-784-字母大小写全排列.py
# 给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以获得一个新的字符串。返回所有可能得到的字符串集合。

# 示例:
# 输入: S = "a1b2"
# 输出: ["a1b2", "a1B2", "A1b2", "A1B2"]

# 输入: S = "3z4"
# 输出: ["3z4", "3Z4"]

# 输入: S = "12345"
# 输出: ["12345"]
# 注意：

# S 的长度不超过12。
# S 仅由数字和字母组成。



class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        ans = []
        l = len(S)
        def dfs(i,s):
            nonlocal S,ans,l
            if i>=l:
                ans.append(s)
                return None

            if S[i].isalpha():
                dfs(i+1,s+S[i].upper())
                dfs(i+1,s+S[i].lower())
            else:
                dfs(i+1,s+S[i])

        dfs(0,"")

        return ans

执行用时为 72 ms 的范例
class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        result = ['']
        
        for x in S:
            if x.isdigit():
                for i in range(len(result)):
                    result[i] = result[i]+x
            else:
                temp = []
                for i in range(len(result)):
                    temp.append(result[i]+x.lower())
                    temp.append(result[i]+x.upper())
                result = temp
        return result
                