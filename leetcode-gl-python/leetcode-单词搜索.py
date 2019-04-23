# leetcode-单词搜索.py
# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。

# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

# 示例:

# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]

# 给定 word = "ABCCED", 返回 true.
# 给定 word = "SEE", 返回 true.
# 给定 word = "ABCB", 返回 false.


"""
思路:
构成??

dfs  and ??

只调用一次啊..

找到首字母,开始遍历搜索..
"""


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rowl = len(board)
        self.ans = False
        
        if rowl<=0 or word == "": return ans

        coll = len(board[0])

        def dfs(r,c,i):
            if self.ans:
                return None

            if i>=len(word):
                self.ans = True 
                return None
            else:
                for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                    if 0<=r+dr<rowl and 0<=c+dc<coll:
                        if board[r+dr][c+dc] ==word[i]:
                            w = board[r+dr][c+dc]

                            board[r+dr][c+dc] = '#'
                            dfs(r+dr,c+dc,i+1)
                            board[r+dr][c+dc] = w

            return None

        initials = word[0]
        for r in range(rowl):
            for c in range(coll):
                if board[r][c]==initials:
                    board[r][c] = '#'
                    dfs(r,c,1)
                    board[r][c] = initials

        return self.ans


# 参考 
# 执行用时为 56 ms 的范例
# class Solution(object):
    
#     def check(self, board, word):
#         b = []
#         w = []
#         for row in range(len(board)):
#             for col in range(len(board[0])):
#                 b.append(board[row][col])
                
#         for i in word:
#             w.append(i)
#         i = 0
#         while i in range(len(w)):
#             if w[i] in b:
#                 b.remove(w[i])
#                 w.remove(w[i])
#             else:
#                 return False
#         if not w:
#             return True
#         else:
#             return False
    
#     def dfs(self, board, word, row, col):
#         first = word[0]
#         word = word[1:]
#         if len(word) == 0:
#             return True
#         board[row][col] = ' '
#         row_next = row + 1
#         row_last = row - 1
#         col_next = col + 1
#         col_last = col - 1
#         if row_next < len(board) and word[0] == board[row_next][col]:
#             if self.dfs(board, word, row_next, col):
#                 return True
#         if row_last >= 0 and word[0] == board[row_last][col]:
#             if self.dfs(board, word, row_last, col):
#                 return True
#         if col_next < len(board[0]) and word[0] == board[row][col_next]:
#             if self.dfs(board, word, row, col_next):
#                 return True
#         if col_last >= 0 and word[0] == board[row][col_last]:
#             if self.dfs(board, word, row, col_last):
#                 return True
#         board[row][col] = first
#         return False
    
#     def exist(self, board, word):
#         """
#         :type board: List[List[str]]
#         :type word: str
#         :rtype: bool
#         """
#         if not word:
#             return True
#         if not board or len(board) == 0 or len(board[0]) == 0:
#             return False
#         if len(word) > len(board)*len(board[0]):
#             return False
#         if self.check(board, word) == False:
#             return False
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 if word[0] == board[i][j]:
#                     if self.dfs(board, word, i, j):
#                         return True
#         return False