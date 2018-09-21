# leetcode-409-最长回文串.py
# 给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。

# 在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。

# 注意:
# 假设字符串的长度不会超过 1010。

# 示例 1:

# 输入:
# "abccccdd"

# 输出:
# 7

# 解释:
# 我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。



"""
思路:
# 从长到短
# 从中到两边

搞错了..这个是构造..

偶数个 随便用

奇数个 选最大
奇数减1 就是偶数了..唉唉唉唉唉唉


"""

from collections import defaultdict

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        ddic = defaultdict(lambda :0)

        for c in s:
            ddic[c] += 1
        print(ddic)

        maxodd = 0
        ans = 0
        for v in ddic.values():
            # 偶数
            if v%2==0:
                ans += v
            else:
                if v>1:
                    ans += v-1
                if v>maxodd:
                    maxodd = 1



        return ans+maxodd

执行用时为 28 ms 的范例
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d={}
        count=0
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in d:
            count+=int(d[i]/2)
        count=count*2
        for i in d:
            if d[i]%2==1:
                count+=1
                break
        return count