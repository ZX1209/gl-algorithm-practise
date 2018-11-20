# leetcode-944-删除列以使之有序.py
# 给出由 N 个小写字母串组成的数组 A，所有小写字母串的长度都相同。

# 现在，我们可以选择任何一组删除索引，对于每个字符串，我们将删除这些索引中的所有字符。

# 举个例子，如果字符串为 "abcdef"，且删除索引是 {0, 2, 3}，那么删除之后的最终字符串为 "bef"。

# 假设我们选择了一组删除索引 D，在执行删除操作之后，A 中剩余的每一列都是有序的。

# 形式上，第 c 列为 [A[0][c], A[1][c], ..., A[A.length-1][c]]

# 返回 D.length 的最小可能值。

 

# 示例 1：

# 输入：["cba","daf","ghi"]
# 输出：1
# 示例 2：

# 输入：["a","b"]
# 输出：0
# 示例 3：

# 输入：["zyx","wvu","tsr"]
# 输出：3
 

# 提示：

# 1 <= A.length <= 100
# 1 <= A[i].length <= 1000


"""
思路:
删除最少的索引..

剩余的每一列都是有序的,,所以要找到无序的列??
"""

class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        l = len(A[0])
        colVals = [[] for _ in range(l)]

        for a in A:
            for i,c in enumerate(a):
                colVals[i].append(ord(c))

        count=0

        for colVal in colVals:
            i = 1
            tmpl = len(colVal)
            while i<tmpl:
                if colVal[i-1]>colVal[i]:
                    break
                i+=1
            if i<tmpl:
                count+=1

        return count

