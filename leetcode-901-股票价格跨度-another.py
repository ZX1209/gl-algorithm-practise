leetcode-901-股票价格跨度.py
# 用户通过次数 7
# 用户尝试次数 29
# 通过次数 7
# 提交次数 57
# 题目难度 Medium
# 编写一个 StockSpanner 类，它收集某些股票的每日报价，并返回该股票当日价格的跨度。

# 今天股票价格的跨度被定义为股票价格小于或等于今天价格的最大连续日数（从今天开始往回数，包括今天）。

# 例如，如果未来7天股票的价格是 [100, 80, 60, 70, 60, 75, 85]，那么股票跨度将是 [1, 1, 1, 2, 1, 4, 6]。

 

# 示例：

# 输入：["StockSpanner","next","next","next","next","next","next","next"], [[],[100],[80],[60],[70],[60],[75],[85]]
# 输出：[null,1,1,1,2,1,4,6]
# 解释：
# 首先，初始化 S = StockSpanner()，然后：
# S.next(100) 被调用并返回 1，
# S.next(80) 被调用并返回 1，
# S.next(60) 被调用并返回 1，
# S.next(70) 被调用并返回 2，
# S.next(60) 被调用并返回 1，
# S.next(75) 被调用并返回 4，
# S.next(85) 被调用并返回 6。

# 注意 (例如) S.next(75) 返回 4，因为截至今天的最后 4 个价格
# (包括今天的价格 75) 小于或等于今天的价格。
 

# 提示：

# 调用 StockSpanner.next(int price) 时，将有 1 <= price <= 10^5。
# 每个测试用例最多可以调用  10000 次 StockSpanner.next。
# 在所有测试用例中，最多调用 150000 次 StockSpanner.next。
# 此问题的总时间限制减少了 50%。


"""
思路,首先,,直接往后推,,效率实在太低了,
于是做了第一个优化,,将重复元素"重叠"起来,
但这样效率还是达不到标准呢..
再优化下,,最大值,,,最小值就不用了..

最后,,嗯,,是不是可以笔记呢..??记录停止的点..就像那个最小栈一样..

"""

class StockSpanner:

    def __init__(self):
        #         数, 笔记, 截至位置
        self.s = [99999,0,0]
        self.l = 3
        self.max = 0
        self.count = 0
    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        self.count += 1

        if price == self.s[-3]:
            self.s[-2] += 1
        else:
            self.s.append(price)
            self.s.append(1)
            self.s.append(0)
            self.l += 3

        if price < self.s[]

        i = self.l
        count = 0
        while i>0:
            if self.s[i-3] > price:
                break
            count += s[i-1]
            i -=2

        return count

# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()
param_1 = obj.next(100)
param_1 = obj.next(80)
param_1 = obj.next(60)
param_1 = obj.next(70)
param_1 = obj.next(75)
param_1 = obj.next()
param_1 = obj.next(100)

