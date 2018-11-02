# leetcode-686-重复叠加字符串匹配.py
# 给定两个字符串 A 和 B, 寻找重复叠加字符串A的最小次数，使得字符串B成为叠加后的字符串A的子串，如果不存在则返回 -1。

# 举个例子，A = "abcd"，B = "cdabcdab"。

# 答案为 3， 因为 A 重复叠加三遍后为 “abcdabcdabcd”，此时 B 是其子串；A 重复叠加两遍后为"abcdabcd"，B 并不是其子串。

# 注意:

#  A 与 B 字符串的长度在1和10000区间范围内。

"""
思路:
B 是否是 A多次重复叠加后的子串..

set
子串
"""

class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if set(A) < set(B):
            return -1

        la = len(A)
        lb = len(B)

        if la>lb:
            if B in A:
                return 1
            elif B in A*2:
                return 2
            else:
                return -1
        else:
            l = max(1,int((lb/la)+0.5))
            if B in A*l:
                return l
            elif B in A*(l+1):
                return l+1
            elif B in A*(l+2):
                return l+2
            else:
                return -1

if __name__ == '__main__':
    A = "abcabcabcabc"
    B = "abac" 
    test = Solution()
    r = test.repeatedStringMatch(A,B)
    print(r)



执行用时为 44 ms 的范例
class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if(A.count(B)>=1):   #count用法
            return 1
        if(set(A)!=set(B)):
            return -1
        if(len(B)>len(A)):
             i=int(len(B)/len(A))
        else:
            i = 2
        while(1):
            C=A*i
            if(C.count(B)>0):
                return i
            if(len(C)>2*len(B)):
                return -1
            i+=1