# # leetcode-合并区间.py
# 给出一个区间的集合，请合并所有重叠的区间。

# 示例 1:

# 输入: [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 示例 2:

# 输入: [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。


"""
思路:
这个还做了一个类呢...

重叠,,
2.start>1.start
1.start<2.end

1.start<2.start
1.end>2.end

可以模拟下..也可以,,
没想全呢..嗯,,
"""


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals,key=lambda x:x.start)

        i = 0
        l = len(intervals)

        while i<len(intervals)-1:
            if intervals[i].start == intervals[i+1].start:
                intervals[i].end = max(intervals[i].end,intervals[i+1].end)
                intervals.pop(i+1)
            elif intervals[i].end>=intervals[i+1].start:
                intervals[i].end = max(intervals[i].end,intervals[i+1].end)
                intervals.pop(i+1)
            else:
                i+=1

        return intervals

执行用时为 44 ms 的范例
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals or len(intervals)<2:return intervals
        start,end = [],[]
        for i in intervals:
            start.append(i.start)
            end.append(i.end)
        start.sort()
        end.sort()
        res,flag1,flag2= [],0,1
        while flag2<len(intervals):
            if start[flag2]>end[flag2-1]:
                res.append(Interval(start[flag1],end[flag2-1]))
                flag1 = flag2
            flag2 += 1
        if flag1!=flag2:
            res.append(Interval(start[flag1],end[flag2-1]))
        return res

执行用时为 48 ms 的范例
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if intervals == []:
            return []
        intervals.sort(key = lambda intervals:intervals.start)
        
        out = []
        out.append([intervals[0].start,intervals[0].end])
        
        for i in range(1,len(intervals)):
            
            if intervals[i].start > out[-1][1]:
                out.append([intervals[i].start,intervals[i].end])
            else:
                out[-1][1] = max(out[-1][1],intervals[i].end)
        
        return out