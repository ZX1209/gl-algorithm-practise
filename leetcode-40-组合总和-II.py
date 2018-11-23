# leetcode-40-组合总和-II.py
# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

# candidates 中的每个数字在每个组合中只能使用一次。

# 说明：

# 所有数字（包括目标数）都是正整数。
# 解集不能包含重复的组合。 
# 示例 1:

# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 所求解集为:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
# 示例 2:

# 输入: candidates = [2,5,2,1,2], target = 5,
# 所求解集为:
# [
#   [1,2,2],
#   [5]
# ]

"""
思路:
范例,思路差不多..呢.



"""


class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        ans = []
        def dfs(target,preList):
            nonlocal candidates,ans
            if target == 0:
                tmpans = sorted(preList)
                if tmpans not in ans:
                    ans.append(tmpans)
                return None
            elif target<0 or len(candidates)<=0:
                return None
            else:
                for i,candidate in enumerate(candidates):
                    candidates.pop(i)
                    keyvalue = target-candidate
                    if keyvalue>=0:
                        dfs(keyvalue,preList+[candidate])
                        candidates.insert(i,candidate)
                    else:
                        candidates.insert(i,candidate)
                        break;



        dfs(target,[])
        return ans


执行用时为 52 ms 的范例
class Solution:
    def combinationSum2(self, candidates, target):
        r = []
        path = []
        candidates.sort()
        self.getPath(candidates, target, [], r,0)
        return r
    def getPath(self, candidates, target, path, r,start):
        if target == 0:

            r.append(path)
            return
        if target < 0:
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > target:
                break
            self.getPath(candidates,target - candidates[i], path + [candidates[i]],
                               r, i+1)
        