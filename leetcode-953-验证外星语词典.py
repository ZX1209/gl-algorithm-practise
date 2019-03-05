# leetcode-953-验证外星语词典.py
# 用户通过次数 8
# 用户尝试次数 13
# 通过次数 8
# 提交次数 14
# 题目难度 Easy
# 某种外星语也使用英文小写字母，但可能顺序 order 不同。字母表的顺序（order）是一些小写字母的排列。

# 给定一组用外星语书写的单词 words，以及其字母表的顺序 order，只有当给定的单词在这种外星语中按字典序排列时，返回 true；否则，返回 false。

 

# 示例 1：

# 输入：words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# 输出：true
# 解释：在该语言的字母表中，'h' 位于 'l' 之前，所以单词序列是按字典序排列的。
# 示例 2：

# 输入：words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# 输出：false
# 解释：在该语言的字母表中，'d' 位于 'l' 之后，那么 words[0] > words[1]，因此单词序列不是按字典序排列的。
# 示例 3：

# 输入：words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# 输出：false
# 解释：当前三个字符 "app" 匹配时，第二个字符串相对短一些，然后根据词典编纂规则 "apple" > "app"，因为 'l' > '∅'，其中 '∅' 是空白字符，定义为比任何其他字符都小（更多信息）。
 

# 提示：

# 1 <= words.length <= 100
# 1 <= words[i].length <= 20
# order.length == 26
# 在 words[i] 和 order 中的所有字符都是英文小写字母。

"""
思路:
赋值..

比较两个依次进行,逆映射
从小到大
"""


class Solution:
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        l = len(words)
        if l<=1:
            return True

        orderdic = dict()
        for i,c in enumerate(order):
            orderdic[c] = i


        def cmp(w1,w2):
            for c1,c2 in zip(w1,w2):
                if orderdic[c1]>orderdic[c2]:
                    return False
                elif orderdic[c1]<orderdic[c2]:
                    return True
                else:
                    continue

            return len(w1)<=len(w2)

        for i in range(l-1):
            if not cmp(words[i],words[i+1]):
                return False

        return True

if __name__ == '__main__':
    words = ["iekm","tpnhnbe"]
    order = "loxbzapnmstkhijfcuqdewyvrg"

    test = Solution()
    r = test.isAlienSorted(words,order)
    print(r)
