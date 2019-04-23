# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 11:46:37 2018

@author: 14049
"""

'''
题目二：运动会分数统计
【问题描述】：参加运动会的n个学校编号为1~n。比赛分成m个男子项目和w个女子项目，项目编号内分别为1~m和m+1~m+w。由于各项目参加人数差别较大，有些项目取前五名，得分顺序为7，5，3，2，1；还有些项目只取前三名，得分顺序为5，3，2。写一个统计程序产生各种成绩单和得分报表。
【基本要求】：产生各学校的成绩单，内容包括各校所取得的各项成绩的项目号、名次（成绩）、姓名和得分；产生团体总分报表，内容包括校号、男子团体总分、女子团体总分和团体总分。
'''

'''
学校
项目
人
名次

学校 人 项目 名次


# 结构
schools
    school
        athletes
            athlete
                gender
                event_results
                    event_result
                        event_id
                        ranking
                    ...
            ...
    ...


# 输入 输出
菜单?
    输入成绩
    输出成绩单


'''

class evnet_result:
    def __init__(self,event_id,rank):
        self.event_id = 
        self.rank = rank
        