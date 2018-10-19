# leetcode-482-密钥格式化.py
# 给定一个密钥字符串S，只包含字母，数字以及 '-'（破折号）。N 个 '-' 将字符串分成了 N+1 组。给定一个数字 K，重新格式化字符串，除了第一个分组以外，每个分组要包含 K 个字符，第一个分组至少要包含 1 个字符。两个分组之间用 '-'（破折号）隔开，并且将所有的小写字母转换为大写字母。

# 给定非空字符串 S 和数字 K，按照上面描述的规则进行格式化。

# 示例 1：

# 输入：S = "5F3Z-2e-9-w", K = 4

# 输出："5F3Z-2E9W"

# 解释：字符串 S 被分成了两个部分，每部分 4 个字符；
#      注意，两个额外的破折号需要删掉。
# 示例 2：

# 输入：S = "2-5g-3-J", K = 2

# 输出："2-5G-3J"

# 解释：字符串 S 被分成了 3 个部分，按照前面的规则描述，第一部分的字符可以少于给定的数量，其余部分皆为 2 个字符。
 

# 提示:

# S 的长度不超过 12,000，K 为正整数
# S 只包含字母数字（a-z，A-Z，0-9）以及破折号'-'
# S 非空

"""
思路:
直接操作??

嗯,,范例,,是很精确呢..
"""

class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.strip('-')
        S = list(S.upper())
        l = len(S)
        i = l-1
        count = 0

        while i>0:
            if S[i] != '-':
                count+=1
                if count>=K:
                    S.insert(i,'-')
                    count=0
            else:
                S.pop(i)

            i-=1
        return "".join(S)

if __name__ == '__main__':
    S = "--a-a-a-a--"
    K = 2
    test = Solution()
    r = test.licenseKeyFormatting(S,K)
    print(r)



执行用时为 44 ms 的范例
class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        a_s = ''.join(S.upper().split('-'))
        length = len(a_s)
        r = []
        first = length % K if length %K != 0 else K
        r.append(a_s[:first])
        for i in range(first, length, K):
            r.append(a_s[i:i+K])
        return '-'.join(r)