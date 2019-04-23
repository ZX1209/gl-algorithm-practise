# leetcode-458-可怜的小猪.py
# 有1000只水桶，其中有且只有一桶装的含有毒药，其余装的都是水。它们从外观看起来都一样。如果小猪喝了毒药，它会在15分钟内死去。

# 问题来了，如果需要你在一小时内，弄清楚哪只水桶含有毒药，你最少需要多少只猪？

# 回答这个问题，并为下列的进阶问题编写一个通用算法。

# 进阶:

# 假设有 n 只水桶，猪饮水中毒后会在 m 分钟内死亡，你需要多少猪（x）就能在 p 分钟内找出“有毒”水桶？n只水桶里有且仅有一只有毒的桶。


"""
思路:
全部试,

部分试,再试. 

主要还是不超限制呢..

先缩小范围,部分喝
除以,,分治.. 

可以缺省一只呢..

对了排除法
2,1,1 之类的..天喽.. 

题目还是有问题
15 分钟死,16分钟测试理论上完不成2次实验的
除非,测试时间结束可以得到没测试完的结果,,但这是.. 

范例是因为导入时间更快的吧.
"""
from math import log, ceil
class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        rounds = minutesToTest//minutesToDie

        return int(ceil(log(buckets)/log(rounds+1)))


执行用时为 20 ms 的范例
class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        temp=minutesToTest/minutesToDie+1
        result=0
        while temp**result<buckets:
            result+=1
        return result