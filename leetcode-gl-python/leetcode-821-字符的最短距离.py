# leetcode-821-字符的最短距离.py
# 给定一个字符串 S 和一个字符 C。返回一个代表字符串 S 中每个字符到字符串 S 中的字符 C 的最短距离的数组。

# 示例 1:

# 输入: S = "loveleetcode", C = 'e'
# 输出: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
# 说明:

# 字符串 S 的长度范围为 [1, 10000]。
# C 是一个单字符，且保证是字符串 S 里的字符。
# S 和 C 中的所有字母均为小写字母。

"""
思路:
寻找,还是状态转移?

范例跟我思路有点像啊..
"""

class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        shortest = []

        prev_C = float('-inf')

        for i,c in enumerate(S):
            if c==C:
                prev_C = i
            shortest.append(i-prev_C)

        next_C = float('inf')
        for i in range(len(S)-1,-1,-1):
            c = S[i]
            if c==C:
                next_C = i 
            shortest[i] = min(shortest[i],next_C-i)

        return shortest












        # ans = []

        # Sp = S.split(C)

        # if len(Sp)<2:
        #     tmp = 0
        #     for c in S:
        #         if c=='e':
        #             tmp = 0
        #             ans.append(tmp)
        #         tmp+=1
        #         ans.append(tmp)
        #     return ans

        # # 奇偶 分开
        # ans.extend([i for i in range(len(tmps[0]),-1,-1) ])

        # ans = []
        # for tmps in Sp[1:-1]:
        #     half = int(len(tmps)/2+0.5)
        #     ans.extend([half-abs(i-half) for i in range(len(tmps),-1,-1) ])

        # ans.extend([i for i in range(0,len(tmps[-1])) ])
        # return ans


执行用时为 44 ms 的范例
class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        record = []
        res = []
        for i in range(0,len(S),1):
            if S[i] == C:
                record.append(i)
        for i in range(0,record[0],1):
            res.append(record[0] - i)
        res.append(0)
        for i in range(0,len(record) - 1,1):
            mid = (record[i+1] + record[i]) // 2
            for j in range(record[i] + 1,mid + 1,1):
                res.append(j - record[i])

            # import 
            for j in range(mid + 1,record[i+1],1):
                res.append(record[i+1] - j)
            
            res.append(0)
        for i in range(record[len(record) - 1] + 1,len(S),1):
            res.append(i -record[len(record) - 1])
        return res