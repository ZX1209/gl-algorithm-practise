# leetcode-890-查找和替换模式.py
class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        lp = len(pattern)
        ans = []

        for word in words:
            if len(word) != lp:
                continue
            else:
                p = {}
                isfailed = 0

                for i in range(lp):
                    # 如果存在映射
                    if pattern[i] in p:
                        # 但是 映射跟词不对,或者,词已经映射过了
                        if p[pattern[i]] != word[i]:
                            isfailed = 1
                            break
                    # 如果 不存在映射
                    else:
                        # 如果词已被映射
                        if word[i] in p.values():
                            isfailed = 1
                            break
                        else:
                            p[pattern[i]] = word[i]

                if not isfailed:
                    ans.append(word)

        return ans

