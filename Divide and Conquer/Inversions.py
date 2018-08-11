#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 21:20:06 2018

@author: Das
"""

def mergeSortInversions(a):
    if len(a) == 1:
        return a, 0
    else:
        Larray = a[:len(a)//2]
        Rarray = a[len(a)//2:]
        
        print(Larray, Rarray)
        
        Larray, Linv = mergeSortInversions(Larray)
        Rarray, Rinv = mergeSortInversions(Rarray)
        Oarray = []
        
        i = 0
        j = 0
        inv = 0 + Linv + Rinv
        
        while i<len(Larray) and j < len(Rarray):
            if Larray[i] <= Rarray[j]:
                Oarray.append(Larray[i])
                i+=1
            else:
                Oarray.append(Rarray[j])
                j+=1
                inv += len(Larray) - i
        Oarray+=Larray[i:]
        Oarray+=Rarray[j:]
        
        print(Oarray)
        return Oarray, inv


'''
For input array [2, 4, 6, 1, 3, 5], there are 6 inversions
For a 6 element array in reverse order there are 15 inversions
Goes by formula n(n-1)/2
Can alsoe be done in quadratic using brute forece nested for loops
'''
print('Enter the numbers seperated by spaces:')
iput = input()

arr = iput.split() 
arr = list(map(int, arr))

output, invCount = mergeSortInversions(arr)