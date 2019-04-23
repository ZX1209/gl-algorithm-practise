# leetcode-769-最多能完成排序的块.py
# 题目描述
# 提示帮助
# 提交记录
# 社区讨论
# 阅读解答
# 数组arr是[0, 1, ..., arr.length - 1]的一种排列，我们将这个数组分割成几个“块”，并将这些块分别进行排序。之后再连接起来，使得连接的结果和按升序排序后的原数组相同。

# 我们最多能将数组分成多少块？

# 示例 1:

# 输入: arr = [4,3,2,1,0]
# 输出: 1
# 解释:
# 将数组分成2块或者更多块，都无法得到所需的结果。
# 例如，分成 [4, 3], [2, 1, 0] 的结果是 [3, 4, 0, 1, 2]，这不是有序的数组。
# 示例 2:

# 输入: arr = [1,0,2,3,4]
# 输出: 4
# 解释:
# 我们可以把它分成两块，例如 [1, 0], [2, 3, 4]。
# 然而，分成 [1, 0], [2], [3], [4] 可以得到最多的块数。
# 注意:

# arr 的长度在 [1, 10] 之间。
# arr[i]是 [0, 1, ..., arr.length - 1]的一种排列。


"""
思路:
数组标号
"""


# 参考
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        min_right = [float('inf')]*len(arr)

        for i in range(len(arr)-2,-1,-1):
            min_right[i] = min(min_right[i+1],arr[i+1])

        partitions = 0
        partition_max = None

        for i,num in enumerate(arr):
            partition_max = num if partition_max is None else max(partition_max,num)

            if partition_max < min_right[i]:
                partitions+=1
                partition_max = None

        return partitions


