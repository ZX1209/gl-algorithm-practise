# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 11:02:58 2018

@author: 14049
"""


import logging as log
import numpy as np

log.basicConfig(format='%(levelname)s:\033[34m %(message)s\033[0m',
level=log.DEBUG)


# %%函数
# 获取 分数
def get_point():
    global matrix
    result=0
    for i in range(9):
        for j in range(9):
            result+=matrix[i][j]*(10-max(abs(i-4),abs(j-4)))


    return result



def  get_col_list(j):
    tmp = []
    for row in matrix:
        tmp.append(row[j])
    return tmp
        
def get_cell_list(i,ii,j,jj):
    tmp = []
    for col in matrix[i:ii]:
        tmp.extend(col[j:jj])
        
    return tmp
    
    

# 映射
# 将位置映射到一个数组(排列好的)上
    
'''
def map_num(num,i,j,ii,jj):
    dis_a=abs(i-j)
    dis_b=abs(ii-jj)
    
    rel_dis=((num-i)/dis_a)
    
    return ii+round(dis_b*rel_dis)
    
# 0 - >  4
# 0->len()-1
def set_num(i,j,list_tmp):
    quan=4-max(abs(i-4),abs(j-4))
    wei=map_num(quan,0,4,0,len(list_tmp)-1)
    
    list_tmp.sort()
    return list_tmp[wei]
'''    
# 获取小格编号
#1 2 3
#4 5 6
#7 8 9 
def get_id(i,j):
    if 3>i>=0:
        if 3>j>=0:
            return 1
        elif 6>j>=3:
            return 2
        else:
            return 3
            
    elif 6>i>=3:
        if 3>j>=0:
            return 4
        elif 6>j>=3:
            return 5
        else:
            return 6
            
    else:
        if 3>j>=0:
            return 7
        elif 6>j>=3:
            return 8
        else:
            return 9
        
def seek_next():
    global matrix
    for i in range(9):
        for j in range(9):
            if matrix[i][j]==0:
                return i,j
    
    return -1,-1
    
# 返回对应单元的现存数字集
def get_cell_set(i,j):
    global matrix
    tmp=get_id(i,j)-1
    ii,jj=int(tmp/3),int(tmp%3)
    ii*=3
    jj*=3
    return set(get_cell_list(ii,ii+3,jj,jj+3))

def get_row_set(i):
    return set(matrix[i])

def get_col_set(j):
    return set(get_col_list(j))


# %%变量


ans = -1

matrix = []


for i in range(9):
    tmp = input().split()
    tmp = list(map(int,tmp))
    matrix.append(tmp)


set_all = set(range(1,10))




# %%深搜树
# 先找找有没有0点
# 之后,填充i,j点的值(i,j还是要0点才行呢)
def p1074dfs(i,j):
    global matrix
    global ans
    
    if i==-1:
        ans = max(ans,get_point())
        return
    
    col_set = get_col_set(j)
    row_set = get_row_set(i)
    cell_set=get_cell_set(i,j)
    
    # 思想不统一真是很麻烦
    set_may = set_all-(row_set | col_set | cell_set)
    
    for pos_val  in list(set_may):
        matrix[i][j]=pos_val
        log.debug('pos:'+str(i)+' '+str(j)+' set to '+ str(pos_val))
        
        nexti,nextj=seek_next()
        p1074dfs(nexti,nextj)
        
        matrix[i][j]=0




starti,startj=seek_next()

p1074dfs(starti,startj)

print(ans)

















#to do 完成数独


        
'''

for i in range(0,9,3):
    for j in range(0,9,3):
        # 遍历整个小区域
        for ai in range(3):
            for aj in range(3):
                if matrix[i+ai,j+aj]==0:
                    set_row = set(matrix[i+ai,:])
                    set_col = set(matrix[:,j+aj])
                    set_land = set(matrix[i:i+3,j:j+3].reshape(1,9)[0,:])
                    set_exit = set_row | set_col | set_land
                    set_diff=set_all.difference(set_exit)
                    
                    # 唯一确定
                    if len(set_diff)>1 :
                        matrix[i+ai,j+aj]=set_num(i+ai,j+aj,list(set_diff))  
                    elif len(set_diff)==1 :
                        matrix[i+ai,j+aj]=set_diff.pop()
                    else:
                        print('-1')
                        #正常退出
                        sys.exit(0)
                else:
                    pass
        
pprint.pprint(matrix)

'''







