#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 23:44:40 2018

@author: Das
"""

def QuickSort(arr, l, r):
    if l < r:
        
        pi = partition(arr, l, r)
        
        QuickSort(arr, l, pi-1)
        QuickSort(arr, pi+1, r)

def partition(a, l, r):
    
    p = a[l]
    i = r + 1
    
    for j in range(r, l, -1):
        if a[j] >= p:
            i-=1
            a[i], a[j] = a[j], a[i]
    a[i-1], a[l] = a[l], a[i-1]
    return i-1


print('Enter numbers to sort separated by space:')
iput = input()

a = iput.split()
a = list(map(int, a))
QuickSort(a, 0, len(a)-1)