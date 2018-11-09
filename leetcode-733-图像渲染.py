# leetcode-733-图像渲染.py
# 有一幅以二维整数数组表示的图画，每一个整数表示该图画的像素值大小，数值在 0 到 65535 之间。

# 给你一个坐标 (sr, sc) 表示图像渲染开始的像素值（行 ，列）和一个新的颜色值 newColor，让你重新上色这幅图像。

# 为了完成上色工作，从初始坐标开始，记录初始坐标的上下左右四个方向上像素值与初始坐标相同的相连像素点，接着再记录这四个方向上符合条件的像素点与他们对应四个方向上像素值与初始坐标相同的相连像素点，……，重复该过程。将所有有记录的像素点的颜色值改为新的颜色值。

# 最后返回经过上色渲染后的图像。

# 示例 1:

# 输入: 
# image = [[1,1,1],[1,1,0],[1,0,1]]
# sr = 1, sc = 1, newColor = 2
# 输出: [[2,2,2],[2,2,0],[2,0,1]]
# 解析: 
# 在图像的正中间，(坐标(sr,sc)=(1,1)),
# 在路径上所有符合条件的像素点的颜色都被更改成2。
# 注意，右下角的像素没有更改为2，
# 因为它不是在上下左右四个方向上与初始点相连的像素点。
# 注意:

# image 和 image[0] 的长度在范围 [1, 50] 内。
# 给出的初始点将满足 0 <= sr < image.length 和 0 <= sc < image[0].length。
# image[i][j] 和 newColor 表示的颜色值在范围 [0, 65535]内。


"""
思路:
嗯,,原先用当前值与周围值比较会陷入无尽的反复修改呢..因为可能后面要改的值,前面就改正确了.之后到要修改它的时候,正确的值要被改为正确呢.
这也是我原先担心的呢..果然递归中还是不要用相对值,,不然就会该乱啊,,毕竟没法保证顺序出错..除非用个备份
"""

class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        s = [(sr,sc)]
        rl = len(image)
        cl = len(image[0])

        if image[sr][sc]==newColor:
            return image
        else:
            oldColor = image[sr][sc]

        while s:
            cr,cc = s.pop()
            for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                if 0<=cr+dr<rl and 0<=cc+dc<cl and oldColor == image[cr+dr][cc+dc]:
                    s.append((cr+dr,cc+dc))

            image[cr][cc] = newColor

        return image


执行用时为 68 ms 的范例
class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        old_color = image[sr][sc]
        pos_stack=[(sr,sc)]
        visited_stack=[]
        while len(pos_stack)>0:
            tmp_pos = pos_stack.pop()
            if tmp_pos in visited_stack:
                continue
            else:
                visited_stack.append(tmp_pos)
            image[tmp_pos[0]][tmp_pos[1]]=newColor
            sr=tmp_pos[0]
            sc=tmp_pos[1]
            if(sr+1<len(image) and image[sr+1][sc]==old_color):
                pos_stack.append((sr+1,sc))
            if(sc-1>=0 and image[sr][sc-1]==old_color):
                pos_stack.append((sr, sc-1))
            if(sr-1>=0 and image[sr-1][sc]==old_color):
                pos_stack.append((sr-1,sc))
            if(sc+1<len(image[0]) and image[sr][sc+1]==old_color):
                pos_stack.append((sr,sc+1))
        return image
            
            