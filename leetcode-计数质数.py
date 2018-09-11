# leetcode-计数质数.py
# 统计所有小于非负整数 n 的质数的数量。

# 示例:

# 输入: 10
# 输出: 4
# 解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。

"""
这,暴力法??

高级点笔记法..

"""

# 官方参考
# 执行用时为 40 ms 的范例
# class Solution:
#     def countPrimes(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
        
#         # isPrime = [True] * max(n, 2)
#         # isPrime[0], isPrime[1] = False, False
#         # x = 2
#         # while x * x < n:
#         #     if isPrime[x]:
#         #         p = x * x
#         #         while p < n:
#         #             isPrime[p] = False
#         #             p += x
#         #     x += 1
#         # return sum(isPrime)
        
        
#         if n == 10000:
#             return 1229
#         if n == 499979:
#             return 41537
#         if n == 999983:
#             return 78497
#         if n == 1500000:
#             return 114155
#         if n <= 2:
#             return 0
        
#         if n == 0 or n == 1:
#             return 0
        
#         count = 0
#         matrix = [True] * n
#         matrix[0] = matrix[1] = False
        
#         i = 2
#         while i < n:
#             if matrix[i] == True:
#                 count += 1
#                 m = i
#                 while m + i < n:
#                     m += i
#                     matrix[m] = False
#             i += 1
    
#         return count



class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        ans = 0
        prime = [0]*n    # 这个是类似状态组的东西
        l = round(n**0.5)    # 最大遍历上限为√n
        for i in range(2, l+1):
            if prime[i]:    # 合数直接过
                continue

            tmpN = (n-i*i)/i
            if tmpN<=0:
                continue

            if tmpN - int(tmpN):
                tmpN = int(tmpN) + 1
            else:
                tmpN = int(tmpN)

            prime[i*i:n:i] = [1] * tmpN
        return n - sum(prime) -2    # 输出总数字与合数的差（-2是去除0 和1）


# def is_primer(n):


#     if n % 6 != 1 and n % 6 != 5:
#          return 0


#     i = 2
#     m = n**(0.5)
#     while i <= m:
#         if n%i == 0 :
#             return 0
#         i += 1

#     return 1

# class Solution:

#     def countPrimes(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         if n<=2:
#             return 0

#         ans = 0
#         i = 2
#         while i<n:
#             if is_primer(i):
#                 ans+=1
#             i+=1

#         return ans

        
if __name__ == '__main__':
    n = 3
    test = Solution()
    r = test.countPrimes(n)
    print(r)




# def is_primer(n):
#     i = 2

#     while i <= n**(1/2):
#         if n%i == 0 :
#             return 0
#         i += 1

#     return 1

# class Solution:
#     def primesNote(self,n):
#         if n in self.note:
#             return self.note[n]
#         else:
#             self.note[n] = is_primer(n-1)+self.primesNote(n-1)
#             return self.note[n]

#     def __init__(self):
#         # init notes
#         self.note = {0:0,1:0,2:0,3:1}

#     def countPrimes(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         if n<2:
#             return 0

#         return self.primesNote(n)
        
# if __name__ == '__main__':
#     n = 100
#     test = Solution()
#     r = test.countPrimes(n)
#     print(r)