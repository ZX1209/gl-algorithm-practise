# leetcode-888-公平的糖果交换.py
class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        dis = (sum(A)-sum(B))/2
        
        A = set(A)
        B = set(B)
        
        for a in A:
            if int(a - dis) in B:
                return [a,int(a-dis)]
   
