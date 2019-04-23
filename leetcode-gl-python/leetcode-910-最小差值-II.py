# leetcode-910-最小差值-II.py
# 用户通过次数 0
# 用户尝试次数 8
# 通过次数 0
# 提交次数 11
# 题目难度 Medium
# 给定一个整数数组 A，对于每个整数 A[i]，我们可以选择 x = -K 或是 x = K，并将 x 加到 A[i] 中。

# 在此过程之后，我们得到一些数组 B。

# 返回 B 的最大值和 B 的最小值之间可能存在的最小差值。

 

# 示例 1：

# 输入：A = [1], K = 0
# 输出：0
# 解释：B = [1]
# 示例 2：

# 输入：A = [0,10], K = 2
# 输出：6
# 解释：B = [2,8]
# 示例 3：

# 输入：A = [1,3,6], K = 3
# 输出：3
# 解释：B = [4,6,3]
 

# 提示：

# 1 <= A.length <= 10000
# 0 <= A[i] <= 10000
# 0 <= K <= 10000


"""
思路:
还是深搜把..
"""



class Solution(object):
    def dfs(self,i):
        if i>=self.l:
            if self.ans>max(self.A)-min(self.A):
                self.ans = max(self.A)-min(self.A)

            return None


        if self.everage - self.A[i]>self.k/2:
            self.A[i]+=self.k
            self.dfs(i+1)
            self.A[i]-=self.k
        elif self.A[i]-self.everage>self.k/2:
            self.A[i]-=self.k
            self.dfs(i+1)
            self.A[i]+=self.k
        else:
            self.A[i]-=self.k
            self.dfs(i+1)
            self.A[i]+=self.k

            self.A[i]+=self.k
            self.dfs(i+1)
            self.A[i]-=self.k

        return None


    def smallestRangeII(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        self.k = K 
        self.l = len(A)
        self.ans = max(A) - min(A)
        self.A = A
        self.everage = sum(A)/self.l


        if 

        self.dfs(0)
        return self.ans














#         minv = min(A)
#         maxv = max(A)
#         tmpans = maxv-minv

#         if (maxv-K)>=(minv+K):
#             return (maxv-K)-(minv+K)
#         else:
#             everage = sum(A)/len(A)
#             B = []
#             for a in A:
#                 if a-everage > K/2:
#                     B.append(a-K)
#                 elif everage -a > K/2:
#                     B.append(a+K)
#                 else:
#                     if a>everage:
#                         a-=K
#                     else:
#                         a+=K
#                     B.append(a)

#             return tmpans if max(B)-min(B) > tmpans else max(B)-min(B)

if __name__ == '__main__':
    A = [2,7,2]
    K = 1
    test = Solution()
    r = test.smallestRangeII(A,K)
    print(r)