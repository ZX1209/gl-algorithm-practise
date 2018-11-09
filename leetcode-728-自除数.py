# leetcode-728-自除数.py
# 自除数 是指可以被它包含的每一位数除尽的数。

# 例如，128 是一个自除数，因为 128 % 1 == 0，128 % 2 == 0，128 % 8 == 0。

# 还有，自除数不允许包含 0 。

# 给定上边界和下边界数字，输出一个列表，列表的元素是边界（含边界）内所有的自除数。

# 示例 1：

# 输入： 
# 上边界left = 1, 下边界right = 22
# 输出： [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
# 注意：

# 每个输入参数的边界满足 1 <= left <= right <= 10000。



class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def splitNum(n):
            ans = []
            while n>0:
                ans.append(n%10)
                n//=10
            return ans

        def isDivingNum(n):
            elements = set(splitNum(n))
            if 0 in elements:
                return False
            else:
                for element in elements:
                    if n%element != 0:
                        return False
                return True

        ans = []

        for n in range(left,right+1):
            if isDivingNum(n):
                ans.append(n)
        return ans


执行用时为 48 ms 的范例
ANSWERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22, 24, 33, 36, 44, 48, 55, 66, 77, 88, 99, 111, 112, 115, 122, 124, 126, 128, 132, 135, 144, 155, 162, 168, 175, 184, 212, 216, 222, 224, 244, 248, 264, 288, 312, 315, 324, 333, 336, 366, 384, 396, 412, 424, 432, 444, 448, 488, 515, 555, 612, 624, 636, 648, 666, 672, 728, 735, 777, 784, 816, 824, 848, 864, 888, 936, 999, 1111, 1112, 1113, 1115, 1116, 1122, 1124, 1128, 1131, 1144, 1155, 1164, 1176, 1184, 1197, 1212, 1222, 1224, 1236, 1244, 1248, 1266, 1288, 1296, 1311, 1326, 1332, 1335, 1344, 1362, 1368, 1395, 1412, 1416, 1424, 1444, 1448, 1464, 1488, 1515, 1555, 1575, 1626, 1632, 1644, 1662, 1692, 1715, 1722, 1764, 1771, 1824, 1848, 1888, 1926, 1935, 1944, 1962, 2112, 2122, 2124, 2128, 2136, 2144, 2166, 2184, 2196, 2212, 2222, 2224, 2226, 2232, 2244, 2248, 2262, 2288, 2316, 2322, 2328, 2364, 2412, 2424, 2436, 2444, 2448, 2488, 2616, 2622, 2664, 2688, 2744, 2772, 2824, 2832, 2848, 2888, 2916, 3111, 3126, 3132, 3135, 3144, 3162, 3168, 3171, 3195, 3216, 3222, 3264, 3276, 3288, 3312, 3315, 3324, 3333, 3336, 3339, 3366, 3384, 3393, 3432, 3444, 3492, 3555, 3612, 3624, 3636, 3648, 3666, 3717, 3816, 3864, 3888, 3915, 3924, 3933, 3996, 4112, 4116, 4124, 4128, 4144, 4164, 4172, 4184, 4212, 4224, 4236, 4244, 4248, 4288, 4332, 4344, 4368, 4392, 4412, 4416, 4424, 4444, 4448, 4464, 4488, 4632, 4644, 4824, 4848, 4872, 4888, 4896, 4932, 4968, 5115, 5155, 5355, 5515, 5535, 5555, 5775, 6126, 6132, 6144, 6162, 6168, 6192, 6216, 6222, 6264, 6288, 6312, 6324, 6336, 6366, 6384, 6432, 6444, 6612, 6624, 6636, 6648, 6666, 6696, 6762, 6816, 6864, 6888, 6912, 6966, 6984, 7112, 7119, 7175, 7224, 7266, 7371, 7448, 7476, 7644, 7728, 7777, 7784, 8112, 8128, 8136, 8144, 8184, 8224, 8232, 8248, 8288, 8328, 8424, 8448, 8488, 8496, 8616, 8664, 8688, 8736, 8824, 8832, 8848, 8888, 8928, 9126, 9135, 9144, 9162, 9216, 9288, 9315, 9324, 9333, 9396, 9432, 9612, 9648, 9666, 9864, 9936, 9999]


class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
#         res = []
#         for i in range(left, right+1):
#             num = i
#             tmp = []
#             tag = True
#             while i != 0:
#                 tmp.append(i % 10)
#                 i //= 10
#             if 0 not in tmp:
#                 for j in tmp:
#                     if num % j != 0:
#                         tag = False
#                         break
#                 if tag == True:
#                     res.append(num)
        
#         return res





#         answer = []
#         for i in range(left, right+1):
#             n = i
#             tag = True
#             while i != 0:
#                 tmp = i%10
#                 if (tmp==0) or (n%tmp!=0):
#                     tag = False
#                     break
#                 i //= 10
                
#             if tag:
#                 answer.append(n)
#         return answer

        return [x for x in ANSWERS if left<=x<=right]