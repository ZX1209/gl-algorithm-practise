# leetcode-599-两个列表的最小索引总和.py
# 假设Andy和Doris想在晚餐时选择一家餐厅，并且他们都有一个表示最喜爱餐厅的列表，每个餐厅的名字用字符串表示。

# 你需要帮助他们用最少的索引和找出他们共同喜爱的餐厅。 如果答案不止一个，则输出所有答案并且不考虑顺序。 你可以假设总是存在一个答案。

# 示例 1:

# 输入:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
# 输出: ["Shogun"]
# 解释: 他们唯一共同喜爱的餐厅是“Shogun”。
# 示例 2:

# 输入:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["KFC", "Shogun", "Burger King"]
# 输出: ["Shogun"]
# 解释: 他们共同喜爱且具有最小索引和的餐厅是“Shogun”，它有最小的索引和1(0+1)。
# 提示:

# 两个列表的长度范围都在 [1, 1000]内。
# 两个列表中的字符串的长度将在[1，30]的范围内。
# 下标从0开始，到列表的长度减1。
# 两个列表都没有重复的元素。


"""
思路:
直接 in  enumerate..
"""

class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        l1 = len(list1)
        l2 = len(list2)
        flag = 0
        ans = []

        for dis in range(l1+l2-1):
            for rdis in range(dis+1):
                if rdis<l1 and dis-rdis<l2 and list1[rdis]==list2[dis-rdis]:
                    flag = 1
                    ans.append(list1[rdis])
            if flag:
                return ans


执行用时为 72 ms 的范例
class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        mapp = {}
        for i, wd in enumerate(list2):
            mapp[wd] = i
        m = len(list1) + len(list2)
        res = []
        for i, wd in enumerate(list1):
            if wd in mapp:
                m = min (mapp[wd] + i , m)
        for i, wd in enumerate(list1):
            if wd in mapp:
                if mapp[wd] + i == m:
                    res.append(wd)
        return res