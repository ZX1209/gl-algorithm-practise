# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 17:43:56 2018

@author: 14049
"""

def isprime(number):
    i=2
    
    while i<number:
        if number%i==0:
            return 1
        
        i+=1
        
    
    if(i*i==number):
        return 0
    else:
        return 1
    
    
def isprime_fast(number):
    if (number==2 or number==3):
        return 1
    
    if(number%6!=1 or number%6!=5):
        return 0
    
    i = 5
    
    while i<=number**(1/2):
        if number%(i)==0 or number%(i+2)==0:
            return 1
        i+=6
        
    return 0
    