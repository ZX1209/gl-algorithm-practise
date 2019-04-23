# leetcode-零钱兑换.py
# 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

# 示例 1:

# 输入: coins = [1, 2, 5], amount = 11
# 输出: 3 
# 解释: 11 = 5 + 5 + 1
# 示例 2:

# 输入: coins = [2], amount = 3
# 输出: -1
# 说明:
# 你可以认为每种硬币的数量是无限的。


"""
思路:
这算是,迭代??


参考 largest_coin???  嗯..
"""
# 参考
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort(reverse = True)
        self.result = float('inf')

        def dfs(largest_coin,remainder,used_coins):
            if remainder == 0:
                self.result = min(self.result,used_coins)
            for i in range(largest_coin,len(coins)):
                if remainder >= coins[i]*(self.result-used_coins):
                    break
                if coins[i] <= remainder:
                    dfs(i,remainder-coins[i],used_coins+1)

        dfs(0,amount,0)

        return self.result if self.result != float('inf') else -1
    # def dfs(self,i,total):
    #     if i>self.count:
    #         return False

    #     if total==0:
    #         if i<self.count:
    #             self.count = i
    #         return True
    #     elif total<0:
    #         return False
    #     else:  
    #         for coin in self.coins:
    #             # if total%coin:
    #             #     if i+(total//coin)<self.count:
    #             #         self.count = i+(total//coin)
    #             # else:
    #             self.dfs(i+1,total-coin)


    # def coinChange(self, coins, amount):
    #     """
    #     :type coins: List[int]
    #     :type amount: int
    #     :rtype: int
    #     """
    #     coins.sort(reverse=True)

    #     s = [amount]
    #     count = amount

    #     while s:
    #         amount = s.pop()
    #         for coin in coins:
    #             while amount-coin>=0:
    #                 amount-=coin
    #                 s.append(amount)

    #             if amount == 0 :
    #                 if len(s)<count:
    #                     count = len(s)

    #     return count















        # if amount<0:
        #     return -1
        # elif len(coins)<=0:
        #     return -1

        # coins.sort(reverse=True)

        # count = 0
        # for coin in coins:
        #     while amount//coin:
        #         amount -=coin
        #         count+=1

        # if amount != 0:
        #     return -1
        # else:
        #     return count


if __name__ == '__main__':
    coins = [1,2,5]
    amount = 11
    test = Solution()
    r = test.coinChange(coins,amount)
    print(r)