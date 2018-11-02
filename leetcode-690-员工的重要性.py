# leetcode-690-员工的重要性.py
# 给定一个保存员工信息的数据结构，它包含了员工唯一的id，重要度 和 直系下属的id。

# 比如，员工1是员工2的领导，员工2是员工3的领导。他们相应的重要度为15, 10, 5。那么员工1的数据结构是[1, 15, [2]]，员工2的数据结构是[2, 10, [3]]，员工3的数据结构是[3, 5, []]。注意虽然员工3也是员工1的一个下属，但是由于并不是直系下属，因此没有体现在员工1的数据结构中。

# 现在输入一个公司的所有员工信息，以及单个员工id，返回这个员工和他所有下属的重要度之和。

# 示例 1:

# 输入: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
# 输出: 11
# 解释:
# 员工1自身的重要度是5，他有两个直系下属2和3，而且2和3的重要度均为3。因此员工1的总重要度是 5 + 3 + 3 = 11。
# 注意:

# 一个员工最多有一个直系领导，但是可以有多个直系下属
# 员工数量不超过2000。



"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""

from functools import lru_cache
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: [Employee]
        :type id: int
        :rtype: int
        """
        dic = {employee.id:employee for employee in employees}
        @lru_cache(maxsize=None)
        def dfs(id):
            nonlocal dic
            tmp = dic[id].importance

            for sub in dic[id].subordinates:
                tmp+=dfs(sub)

            return tmp
        return dfs(id)



× 关闭
执行用时为 212 ms 的范例
"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def __init__(self):
        self.res=0
        self.importances = {}   
        self.subordinates = {}
    
    def calculate_value(self,employees,ids):
        for id in ids:
            self.res += self.importances[id]
            self.calculate_value(employees,self.subordinates[id])
    
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """     
        for employee in employees:
            self.importances[employee.id]=employee.importance
            self.subordinates[employee.id]=employee.subordinates
        ids = self.subordinates[id]
        self.res += self.importances[id]
        self.calculate_value(employees,ids)
        return self.res
        
        