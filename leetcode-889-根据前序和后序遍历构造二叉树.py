leetcode-889-根据前序和后序遍历构造二叉树.py

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def preorder(h):
    if h == None:
        return 0

    print(h.val, ',', end='')

    preorder(h.left)
    preorder(h.right)


def postorder(h):
    if h == None:
        return 0

    postorder(h.left)
    postorder(h.right)

    print(h.val, ',', end='')


def middleorder(h):
    if h == None:
        return 0

    middleorder(h.left)
    print(h.val, ',', end='')
    middleorder(h.right)


def buildtree(tp, pre, post):
    if len(pre) == 1:
        tp = TreeNode(pre[0])
        return tp

    if pre[1] == post[1]:
        tp = TreeNode(pre[0])
        tp.left = buildtree(tp.left, pre[1:], post[1:])
        return tp

    tp = TreeNode(pre[0])
    tmpl = pre[1]
    tmpr = post[1]

    try:
        prer = pre.index(tmpr)
        postl = post.index(tmpl)

        lpre = pre[1:prer]
        rpre = pre[prer:]

        rpost = post[1:postl]
        lpost = post[postl:]

    except ValueError:
        return None

    tp.left = buildtree(tp.left, lpre, lpost)
    tp.right = buildtree(tp.right, rpre, rpost)

    return tp


def class_test(c):
	c.left = TreeNode(10)
	c.right = TreeNode(20)
	return 0 

def python_test(l, length):
    if length < 10:
        print(length, l)
        l.append(length)
    	python_test(l, length+1)
    return 0

def change_test(l, length):
    if length < 10:
        print(length, l)
        l[length] = 0
    	python_test(l, length+1)
    return 0

def poplist(l):
	if len(l)>=1:
		print(l)
		l.pop()
		poplist(l)

	return 0 

def appendlist(l):
	if len(l)<10:
		print(l)
		l.append(len(l))
		appendlist(l)

	return 0 

class Solution:
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        post = post[::-1]
        head = buildtree(head, pre, post)
