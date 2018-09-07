# leetcode-有效的字母异位词.py


class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        else:
            if set(s) != set(t):
                return False
            else:
                for c in set(s):
                    if s.count(c) != t.count(c):
                        return False

                return True

        # return set(s) == set(t) and all(s.count(i) == t.count(i) for i in set(s))

