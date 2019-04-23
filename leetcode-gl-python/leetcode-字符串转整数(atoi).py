# leetcode-字符串转整数(atoi).py


class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        length = len(str)
        i = 0
        tmps = ""

        while i < length:
            if str[i] != " ":
                break
            i += 1
        if i>=length:
            return 0

        if str[i] == '+' or str[i] == '-' or ord('0') <= ord(str[i]) <= ord('9'):
            tmps += str[i]
            i += 1
        else:
            return 0

        while i < length:
            if ord('0') <= ord(str[i]) <= ord('9'):
                tmps += str[i]
            else:
                break

            i += 1

        if len(tmps) > 1:
            tmpint = int(tmps)
            if -2147483648 >= tmpint:
                return -2147483648
            elif tmpint >= 2147483647:
                return 2147483647
            else:
                return tmpint
                
        else:
            if tmps.isnumeric():
                return int(tmps)
            else:
                return 0


if __name__ == '__main__':
    test = Solution()
    print(test.myAtoi("42"))
