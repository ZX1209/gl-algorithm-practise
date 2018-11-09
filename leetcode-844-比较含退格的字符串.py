# leetcode-844-比较含退格的字符串.py
# 给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。

 

# 示例 1：

# 输入：S = "ab#c", T = "ad#c"
# 输出：true
# 解释：S 和 T 都会变成 “ac”。
# 示例 2：

# 输入：S = "ab##", T = "c#d#"
# 输出：true
# 解释：S 和 T 都会变成 “”。
# 示例 3：

# 输入：S = "a##c", T = "#a#c"
# 输出：true
# 解释：S 和 T 都会变成 “c”。
# 示例 4：

# 输入：S = "a#c", T = "b"
# 输出：false
# 解释：S 会变成 “c”，但 T 仍然是 “b”。
 

# 提示：

# 1 <= S.length <= 200
# 1 <= T.length <= 200
# S 和 T 只含有小写字母以及字符 '#'。



class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        st = []
        tt = []

        for s in S:
            if s=='#':
                if len(st)>0:
                    st.pop()
            else:
                st.append(s)

        for t in T:
            if t=='#':
                if len(tt)>0:
                    tt.pop()
            else:
                tt.append(t)

        return "".join(st) == "".join(tt)


执行用时为 36 ms 的范例
class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        
        def clear(s):
            sS = []
            for c in s:
                if c!='#':
                    sS.append(c)
                else:
                    if sS:
                        sS.pop()
            return sS
        
        return clear(S) == clear(T)