# leetcode-Fizz_Buzz.py
# 写一个程序，输出从 1 到 n 数字的字符串表示。

# 1. 如果 n 是3的倍数，输出“Fizz”；

# 2. 如果 n 是5的倍数，输出“Buzz”；

# 3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。

# 示例：

# n = 15,

# 返回:
# [
#     "1",
#     "2",
#     "Fizz",
#     "4",
#     "Buzz",
#     "Fizz",
#     "7",
#     "8",
#     "Fizz",
#     "Buzz",
#     "11",
#     "Fizz",
#     "13",
#     "14",
#     "FizzBuzz"
# ]

"""
思路:
嗯,,数字转字符串吗??

参考只是比我做了更少的判断而已
"""

class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        ans = []

        for i in range(1,n+1):
            # n%3 与 n%5 同时为真
            # 即都不能整除
            if i%3 and i%5:
                ans.append(str(i))
            else:
                tmps = ""
                if i%3==0:
                    tmps+="Fizz"

                if i%5==0:
                    tmps+="Buzz"

                ans.append(tmps)


        return ans

if __name__ == '__main__':
    n=15
    test = Solution()
    r = test.fizzBuzz(n)
    print(r)


# 参考
# 执行用时为 52 ms 的范例
# class Solution:
#     def fizzBuzz(self, n):
#         """
#         :type n: int
#         :rtype: List[str]
#         """
#         L = []
        
#         for i in range(1, n+1):
#             if i % 15 == 0:
#                 L.append('FizzBuzz')
#             elif i % 3 == 0:
#                 L.append('Fizz')
#             elif i % 5 == 0:
#                 L.append('Buzz')
#             else:
#                 L.append(str(i))
                
#         return L