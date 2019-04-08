# 777. 在LR字符串中交换相邻字符
# 题目描述提示帮助提交记录社区讨论阅读解答
# 在一个由 'L' , 'R' 和 'X' 三个字符组成的字符串（例如"RXXLRXRXL"）中进行移动操作。一次移动操作指用一个"LX"替换一个"XL"，或者用一个"XR"替换一个"RX"。现给定起始字符串start和结束字符串end，请编写代码，当且仅当存在一系列移动操作使得start可以转换成end时， 返回True。

# 示例 :

# 输入: start = "RXXLRXRXL", end = "XRLXXRRLX"
# 输出: True
# 解释:
# 我们可以通过以下几步将start转换成end:
# RXXLRXRXL ->
# XRXLRXRXL ->
# XRLXRXRXL ->
# XRLXXRRXL ->
# XRLXXRRLX
# 注意:

# 1 <= len(start) = len(end) <= 10000。
# start和end中的字符串仅限于'L', 'R'和'X'。

"""
思路:
R 向→
L 向←

数量

位置
"""
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        sl = len(start)
        el = len(end)
        si = 0
        ei = 0

        while si<sl and ei <el:
            while si<sl:
                if start[si] != 'X':
                    break
                si+=1

            while ei<el:
                if end[ei] != 'X':
                    break
                ei+=1

            if si>=sl and ei>=el:
                return True
            elif si>=sl or ei >= el:
                return False

            if start[si]==end[ei]:
                if start[si]=='L'and si<ei:
                    return False
                elif start[si]=='R'and si>ei:
                    return False
            else:
                return False

            si+=1
            ei+=1

        return True

if __name__ == '__main__':
    start = "RXXLRXRXL"
    end = "XRLXXRRLX"
    test = Solution()
    r = test.canTransform(start,end)
    print(r)