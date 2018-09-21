# leetcode-401-二进制手表.py
# 二进制手表顶部有 4 个 LED 代表小时（0-11），底部的 6 个 LED 代表分钟（0-59）。

# 每个 LED 代表一个 0 或 1，最低位在右侧。



# 例如，上面的二进制手表读取 “3:25”。

# 给定一个非负整数 n 代表当前 LED 亮着的数量，返回所有可能的时间。

# 案例:

# 输入: n = 1
# 返回: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
 

# 注意事项:

# 输出的顺序没有要求。
# 小时不会以零开头，比如 “01:00” 是不允许的，应为 “1:00”。
# 分钟必须由两位数组成，可能会以零开头，比如 “10:2” 是无效的，应为 “10:02”。


"""
思路:
处理小时中的0

先是,时间的输出

如何构造时间?

如何,形成全部可能

先是,1,2,4...的可能情况

深搜?
+0+1...

范例用可能性 积 可以参考下
""" 

def isValidTime(bins):
    if int(bins[:4],2) <=11 and int(bins[4:],2) <= 59:
        return True
    else:
        return False

def binsToTimes(bins):
    hours = str(int(bins[:4],2))
    mins = str(int(bins[4:],2)) 
    if len(mins) <2:
        mins  = "0" + mins

    return hours+":"+mins




class Solution(object):
    def dfs(self,bins,n):
        if n == 0:
            bins = bins + "0"*(10-len(bins))
            if isValidTime(bins):
                self.ans.append(binsToTimes(bins))
                return None

        if len(bins)>=10:
            return None

        # n!=0 and len(l)<12

        self.dfs(bins+"1",n-1)
        self.dfs(bins+"0",n)


    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        if num<=0:
            return ["0:00"]

        self.ans = []

        self.dfs("",num)

        return self.ans


# 执行用时为 24 ms 的范例
# class Solution(object):
#     def readBinaryWatch(self, num):
#         """
#         :type num: int
#         :rtype: List[str]
#         """
#         a={0: ['0'], 1: ['1', '2', '4', '8'], 2: ['3', '5', '6', '9', '10'], 3: ['7', '11']}
#         b={0: ['00'], 1: ['01', '02', '04', '08', '16', '32'], 2: ['03', '05', '06', '09', '10', '12', '17', '18', '20', '24', '33', '34', '36', '40', '48'], 3: ['07', '11', '13', '14', '19', '21', '22', '25', '26', '28', '35', '37', '38', '41', '42', '44', '49', '50', '52', '56'], 4: ['15', '23', '27', '29', '30', '39', '43', '45', '46', '51', '53', '54', '57', '58'], 5: ['31', '47', '55','59']}
#         if num<0 or num>8:
#             return []
#         mi=max(0,num-5)
#         mx=min(3,num)
#         res=[]
#         for i in range(mi,mx+1):
#             for x in a[i]:
#                 for y in b[num-i]:
#                     res.append(x+':'+y)
#         return res