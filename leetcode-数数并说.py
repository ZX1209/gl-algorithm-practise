# leetcode-数数并说.py

class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        i = 1
        preline = "1"
        nextline = "1"

        while i < n:
            preline = nextline
            nextline = ""
            
            count = 0
            thenum = preline[0]
            index = 0
            while True:
                while index < len(preline) and preline[index] == thenum:
                    index += 1
                    count += 1

                if index >= len(preline):
                    nextline = nextline + str(count) + str(thenum)
                    break

                # below preline[i] != thenum
                nextline = nextline + str(count) + str(thenum)
                thenum = preline[index]
                count = 0

            i += 1

        return nextline


# if __name__ == '__main__':
#     test = Solution()
#     for _ in range(10):
#         print(test.countAndSay(_))

# 参考
# class Solution:
#     def countAndSay(self, n):
#         """
#         :type n: int
#         :rtype: str
#         """
#         index = 1
#         string = '1'
#         while index < n:
#             num = 0
#             nextStr = ''
#             prech = string[0]
#             for ch in string:
#                 if ch == prech:
#                     num += 1
#                 else:
#                     nextStr += (str(num)+prech)
#                     num = 1
#                     prech = ch
#             nextStr += (str(num)+prech)
#             string = nextStr
#             index += 1
#         return string