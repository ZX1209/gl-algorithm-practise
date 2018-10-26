# leetcode-606-根据二叉树创建字符串.py
# 你需要采用前序遍历的方式，将一个二叉树转换成一个由括号和整数组成的字符串。

# 空节点则用一对空括号 "()" 表示。而且你需要省略所有不影响字符串与原始二叉树之间的一对一映射关系的空括号对。

# 示例 1:

# 输入: 二叉树: [1,2,3,4]
#        1
#      /   \
#     2     3
#    /    
#   4     

# 输出: "1(2(4))(3)"

# 解释: 原本将是“1(2(4)())(3())”，
# 在你省略所有不必要的空括号对之后，
# 它将是“1(2(4))(3)”。
# 示例 2:

# 输入: 二叉树: [1,2,3,null,4]
#        1
#      /   \
#     2     3
#      \  
#       4 

# 输出: "1(2()(4))(3)"

# 解释: 和第一个示例相似，
# 除了我们不能省略第一个对括号来中断输入和输出之间的一对一映射关系。

"""
思路:
看题!!
"""


class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ""
        self.str = []

        def dfs(t):
            if not t:
                return None

            self.str.append(str(t.val))
            if t.right or t.left:
                self.str.append('(')
                dfs(t.left)
                self.str.append(')')

            if t.right:
                self.str.append('(')
                dfs(t.right)
                self.str.append(')')

        dfs(t)
        # print("".join(self.str))

        # l = len(self.str)
        # i = l-1
        # while i>0:
        #     if self.str[i]==')' and self.str[i-1]=='(':
        #         self.str.pop(i)
        #         self.str.pop(i-1)
        #         i-=1
        #     i-=1

        return "".join(self.str)
