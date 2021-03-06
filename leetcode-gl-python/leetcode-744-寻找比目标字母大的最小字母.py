# leetcode-744-寻找比目标字母大的最小字母.py
# 给定一个只包含小写字母的有序数组letters 和一个目标字母 target，寻找有序数组里面比目标字母大的最小字母。

# 数组里字母的顺序是循环的。举个例子，如果目标字母target = 'z' 并且有序数组为 letters = ['a', 'b']，则答案返回 'a'。

# 示例:

# 输入:
# letters = ["c", "f", "j"]
# target = "a"
# 输出: "c"

# 输入:
# letters = ["c", "f", "j"]
# target = "c"
# 输出: "f"

# 输入:
# letters = ["c", "f", "j"]
# target = "d"
# 输出: "f"

# 输入:
# letters = ["c", "f", "j"]
# target = "g"
# 输出: "j"

# 输入:
# letters = ["c", "f", "j"]
# target = "j"
# 输出: "c"

# 输入:
# letters = ["c", "f", "j"]
# target = "k"
# 输出: "c"
# 注:

# letters长度范围在[2, 10000]区间内。
# letters 仅由小写字母组成，最少包含两个不同的字母。
# 目标字母target 是一个小写字母。


"""
思路:
二分查找,,没想到呢..
"""


class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if letters[-1]<=target or letters[0]>target:
            return letters[0]

        ans = 'z'
        for letter in letters:
            if letter>target and letter<ans:
                ans = letter
        return ans




执行用时为 44 ms 的范例
class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        length = len(letters)
        if target >= letters[length-1]:
            return letters[0]
        else:
            start = 0
            end = length -1
            while end >= start:
                mid = int((end+start)/2)
                if letters[mid]>target:
                    end = mid-1
                elif letters[mid]<target:
                    start = mid+1
                else:
                    while letters[mid] == target:
                        mid+=1
                    return letters[mid]
            return letters[start]
        