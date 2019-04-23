
# def main(x):
#     if x<0:
#         return 'false'
#     else:
#         tmpx = x
#         wei = 0

#     ## 可以优化一半
#     while tmpx!=0:
#         tmpx = int(tmpx/10)
#         wei+=1

#     half = int(wei/2)

        
#     tmpx = x
#     tmps = 0
#     tmphalf = half
#     while tmphalf!=0:
#         tmp = tmpx%10
#         tmps = tmps*10+tmp
#         tmpx = int(tmpx/10)
#         tmphalf-=1
        
#     print(x,wei,half,int(x/(10**(wei-half))),tmps)

#     if int(x/(10**(wei-half)))==tmps:
#         return 'true'
#     else:
#         return 'false'

def main(x):
    if x<0:
        return False
    else:
        left = x
        right = 0
        while left>right:
            right = right*10+left%10
            left = int(left/10)
            print(left,right)
        
        print(x,left,right)
        
        if left==right or left==right/10: 
            return True
        else:
            return False


if __name__ == '__main__':
    main(121)