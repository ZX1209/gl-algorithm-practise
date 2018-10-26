# leetcode-572-另一个树的子树.py
# 给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s 也可以看做它自身的一棵子树。

# 示例 1:
# 给定的树 s:

#      3
#     / \
#    4   5
#   / \
#  1   2
# 给定的树 t：

#    4 
#   / \
#  1   2
# 返回 true，因为 t 与 s 的一个子树拥有相同的结构和节点值。

# 示例 2:
# 给定的树 s：

#      3
#     / \
#    4   5
#   / \
#  1   2
#     /
#    0
# 给定的树 t：

#    4
#   / \
#  1   2
# 返回 false。

"""
思路:
转化为string sub啊..
"""

from collections import defaultdict

class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        nodes = [s]
        slist = []
        while nodes:
            node = nodes.pop()
            slist.append(node.val)
            if node.left : 
                nodes.append(node.left)
            else:
                slist.append(str(node.val)+"left")

            if node.right : 
                nodes.append(node.right)
            else:
                slist.append(str(node.val)+"right")

        tlist = []
        nodes = [t]
        while nodes:
            node = nodes.pop()
            tlist.append(node.val)
            if node.left : 
                nodes.append(node.left)
            else:
                tlist.append(str(node.val)+"left")

            if node.right : 
                nodes.append(node.right)
            else:
                tlist.append(str(node.val)+"right")

        def findsub(s1,s2):
            """s1 中 找 s2
            """
            l1 = len(s1)
            l2 = len(s2)
            dic = defaultdict(int)
            i = 0
            for i in range(l2):
                dic[s2[i]]-=1
                dic[s1[i]]+=1

            i+=1
            while i<l1:
                if any(dic.values()):
                    # print(dic)
                    dic[s1[i]]+=1
                    dic[s1[i-l2]]-=1
                    i+=1
                else:
                    return True 

            return not any(dic.values())
        # print(slist,tlist)
        return findsub(slist,tlist)




执行用时为 104 ms 的范例
class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        """
        def serialize(root):
            ans = []
            stack = [(root, 1)]
            while stack:
                node, p = stack.pop()
                if not node:
                    ans.append("#")
                    continue
                if p == 0:
                    ans.append("|" + str(node.val))
                else:
                    stack.append((node.right, 1))
                    stack.append((node.left, 1))
                    stack.append((node, 0))
            return ",".join(ans)
        return serialize(t) in serialize(s)
        """
        
        def dfs(node, alist=None):
            if alist is None:
                alist = []
            
            if node.left is None:
                alist.append('L')
            else:
                dfs(node.left, alist)
                
            alist.append(str(node.val))
            
            if node.right is None:
                alist.append('R')
            else:
                dfs(node.right, alist)
            
            return alist
        
        self.slist = dfs(s)
        self.tlist = dfs(t)
        sStr = ''.join(self.slist)
        tStr = ''.join(self.tlist)

        return tStr in sStr      
