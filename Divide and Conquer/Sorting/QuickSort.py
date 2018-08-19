#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 22:36:45 2018

@author: Das
"""

def Quicksort(arr, l, r):
    if l < r:
        pi = partition(arr, l, r)
        
        arr = Quicksort(arr, l, pi-1)
        arr = Quicksort(arr, pi+1, r)
    return arr
        
def partition(a, l, r):
    p = a[r]
    i = l-1
    
    for j in range(l, r):
        if a[j] <= p:
            i+=1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[r] = a[r], a[i+1]
    return i+1
    

print('Enter numbers to sort separated by space:')
iput = input()

a = iput.split()
a = list(map(int, a))
a = Quicksort(a, 0, len(a)-1)

print(list(range(0, 6)))