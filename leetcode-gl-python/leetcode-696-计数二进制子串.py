# leetcode-696-计数二进制子串.py
# 给定一个字符串 s，计算具有相同数量0和1的非空(连续)子字符串的数量，并且这些子字符串中的所有0和所有1都是组合在一起的。

# 重复出现的子串要计算它们出现的次数。

# 示例 1 :

# 输入: "00110011"
# 输出: 6
# 解释: 有6个子串具有相同数量的连续1和0：“0011”，“01”，“1100”，“10”，“0011” 和 “01”。

# 请注意，一些重复出现的子串要计算它们出现的次数。

# 另外，“00110011”不是有效的子串，因为所有的0（和1）没有组合在一起。
# 示例 2 :

# 输入: "10101"
# 输出: 4
# 解释: 有4个子串：“10”，“01”，“10”，“01”，它们具有相同数量的连续1和0。
# 注意：

# s.length 在1到50,000之间。
# s 只包含“0”或“1”字符。

"""
思路:
组合在一起..

左边,右边??
"""

class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def findall(s,substr):
            i = -1
            tmp = []
            l = len(s)
            while i<l:
                i = s.find(substr,i+1)
                if i==-1:
                    break
                tmp.append(i)

            return tmp

        leftones = findall(s,'10')
        rightones = findall(s,'01')
        l = len(s)

        count=0

        for leftone in leftones:
            left = leftone
            right = leftone+1

            while left>=0 and right<l:
                if s[left]=='1' and s[right]=='0':
                    count+=1
                    left-=1
                    right+=1
                else:
                    break

        for rightone in rightones:
            left = rightone
            right = rightone+1

            while left>=0 and right<l:
                if s[left]=='0' and s[right]=='1':
                    count+=1
                    left-=1
                    right+=1
                else:
                    break

        return count

        # l = len(s)
        # i = 1
        # ans = 0
        # while i*2<=l:
        #     ans+=s.count('0'*i+'1'*i)
        #     ans+=s.count('1'*i+'0'*i)
        #     i+=1
        # return ans


#执行用时为 152 ms 的范例
class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        tot_0, tot_1, res, pre_s = 0, 0, -1, ''
        for i in s:
            if i == pre_s:
                if i == '1':
                    tot_1 += 1
                    if tot_1 <= tot_0:
                        res += 1
                else:
                    tot_0 += 1
                    if tot_0 <= tot_1:
                        res += 1
            else:
                if i == '1':
                    tot_1 = 1
                else:
                    tot_0 = 1
                res += 1
            pre_s = i

        return res

#执行用时为 156 ms 的范例
class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        tot_0, tot_1, res, pre_s = 0, 0, -1, ''
        for i in s:
            if i == pre_s:
                if i == '1':#如果目前的字符和上一个字符一样，并且属于000.....1111....的形式那么每多一个1就多一个子串的可能
                    tot_1 += 1
                    if tot_1 <= tot_0:
                        res += 1
                else:#如果目前的字符和上一个字符一样，并且属于1111.....0000....的形式那么每多一个0就多一个子串的可能
                    tot_0 += 1
                    if tot_0 <= tot_1:
                        res += 1
            else:#在0，1的交界处重新计算0，1的数量，同时子串的个数+1
                if i == '1':
                    tot_1 = 1
                else:
                    tot_0 = 1
                res += 1
            pre_s = i

        return res


if __name__ == '__main__':
    s = '1110000110'
    test = Solution()
    r = test.countBinarySubstrings(s)
    print(r)