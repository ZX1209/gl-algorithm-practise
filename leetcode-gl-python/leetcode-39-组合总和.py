# leetcode-39-组合总和.py
# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

# candidates 中的数字可以无限制重复被选取。

# 说明：

# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。 
# 示例 1:

# 输入: candidates = [2,3,6,7], target = 7,
# 所求解集为:
# [
#   [7],
#   [2,2,3]
# ]
# 示例 2:

# 输入: candidates = [2,3,5], target = 8,
# 所求解集为:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]

"""
思路:
所有数都是正整数

重复组合..

递归??

整除

可以剪枝优化..呀
"""


class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        def dfs(target,preList):
            nonlocal candidates,ans
            if target<0:
                return None
            elif target == 0:
                tmpans = sorted(preList)
                if tmpans not in ans:
                    ans.append(tmpans)
                return None
            else:
                for candidate in candidates:
                    dfs(target-candidate,preList+[candidate])
        dfs(target,[])
        return ans

执行用时为 64 ms 的范例
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        def findSum(cans, tar):
            result_list = []
            for i, can in enumerate(cans):
                # print(cans, tar)
                can = cans[i]
                if tar == can:
                    result_list.append([can])
                elif tar > can:
                    found = findSum(cans[i:], tar - can)
                    if found:
                        for sum_list in found:
                            sum_list.append(can)
                            result_list.append(sum_list)
                else:
                    return result_list
            return result_list
        return findSum(candidates, target)
                        
        
 