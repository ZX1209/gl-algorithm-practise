# leetcode-26-删除排序数组中的重复项.py
# 题目描述提示帮助提交记录社区讨论阅读解答
# 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

# 示例 1:

# 给定数组 nums = [1,1,2], 

# 函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。 

# 你不需要考虑数组中超出新长度后面的元素。
# 示例 2:

# 给定 nums = [0,0,1,1,1,2,2,3,3,4],

# 函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。

# 你不需要考虑数组中超出新长度后面的元素。
# 说明:

# 为什么返回数值是整数，但输出的答案是数组呢?

# 请注意，输入数组是以“引用”方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

# 你可以想象内部操作如下:

# // nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
# int len = removeDuplicates(nums);

# // 在函数里修改输入数组对于调用者是可见的。
# // 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
# for (int i = 0; i < len; i++) {
#     print(nums[i]);
# }

"""
思路..
"""

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l = len(nums)
        if l<=1:
            return l

        current = 0
        n = 1

        while current<l and n<l:
            while n < l and nums[current] ==  nums[n]:
                n += 1

            if n >= l:
                break


            nums[current+1] = nums[n]

            current += 1

        return current+1


if __name__ == '__main__':
    test = Solution()
    l = [1,1,1,1,2,3,5,5]
    o = test.removeDuplicates(l)
    print(o)
    print(l)



# 参考
# 执行用时为 60 ms 的范例
# class Solution:
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if len(nums) < 2:
#             return len(nums)
#         # nums >= 2
#         index = 1
#         pre = nums[0]
#         for i in range(len(nums)):
#             if pre != nums[i]:
#                 pre = nums[i]
#                 nums[index] = pre
#                 index += 1
#         return index