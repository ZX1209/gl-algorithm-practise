# leetcode-374-猜数字大小.py
# 我们正在玩一个猜数字游戏。 游戏规则如下：
# 我从 1 到 n 选择一个数字。 你需要猜我选择了哪个数字。
# 每次你猜错了，我会告诉你这个数字是大了还是小了。
# 你调用一个预先定义好的接口 guess(int num)，它会返回 3 个可能的结果（-1，1 或 0）：

# -1 : 我的数字比较小
#  1 : 我的数字比较大
#  0 : 恭喜！你猜对了！
# 示例 :

# 输入: n = 10, pick = 6
# 输出: 6


"""
思路:
二分

题目错了...,,fuck,,返回值反了过来.
"""




# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

def guess(num):
    if num==6:
        return 0
    elif num>6:
        return 1
    elif num<6:
        return -1

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = n//2
        left = 0
        right = n+1

        while True:
            tmp = guess(ans)
            print(ans,tmp)

            if tmp == 0:
                break
            elif tmp == 1:
                left = ans
                ans = (right+ans)//2
            elif tmp == -1:
                right = ans
                ans  = (left+ans)//2

        return ans


if __name__ == '__main__':
    num = 10
    test = Solution()
    r = test.guessNumber(num)
    print(r)


# 参考
# 执行用时为 20 ms 的范例
# # The guess API is already defined for you.
# # @param num, your guess
# # @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# # def guess(num):

# class Solution(object):
#     def guessNumber(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         left = 1
#         right = n
#         ii = int((left+right)/2)
#         while True:
#             if guess(ii) == 0:
#                 return ii
#             if guess(ii) == 1:
#                 left = ii
#                 if ii != int((left+right)/2):
#                     ii = int((left+right)/2)
#                 else:
#                     ii += 1
#             elif guess(ii) == -1:
#                 right = ii