
def removeDuplicates( nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    current = 0
    for i in range(len(nums)):
        if nums[i]<=nums[current]:
            continue
        else:
            current+=1
            nums[current] = nums[i]

    return current+1

print(removeDuplicates([1, 1, 2]))


def reverseInt(tmpint):
    rint = 0
    while (tmpint / 10)>=1:
        rint = rint * 10 + tmpint % 10
        tmpint = int(tmpint/10)

    rint = rint * 10 + tmpint % 10
    return rint


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0:
            return 0
        elif x>0:
            rint =  reverseInt(x)
        else:
            rint =  0-reverseInt(-x)
        
        if -2147483648<=rint<=2147483647:
            return rint
        else:
            return 0
# class Solution:
#     def reverse(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
#         rint = 0
#         if x>=0:
#             rint =  int(str(x)[::-1])
#         else:
#             rint =  0-int(str(abs(x))[::-1])
        
#         if -2147483648<=rint<=2147483647:
#             return rint
#         else:
#             return 0


class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        foundRepeat = 0

        for i in range(length):
            for j in range(i + 1, length):
                if s[j] == s[i]:
                    foundRepeat = 1
                    break
            if not foundRepeat:
                res = i

        return res

        # while i<len(nums):
        #     # find and replace
        #     while i<len(nums) and nums[i]<=nums[current]:
        #         i+=1

        #     if i == len(nums):
        #         break

        #     current += 1
        #     nums[current] = nums[i]

        # return current+1
        # 找到下一个不重复元素
        



        # # for range 算是固定换引用的...
        # while i < len(nums):
        #     while nums[i]<=current:
        #         i = i + 1

        #     # 类似
        #     # for j in range(i,len(nums)):
        #     #     if nums[j]>current:
        #     #         i = j
        #     #         break
        #     # 找到 i 使得 nums[i]> current
        #     # 这就是不重复的下一位


        #     nums[i] = nums[i + 1]
        #     current = nums[i]
