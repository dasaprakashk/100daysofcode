#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 00:06:50 2018

@author: Das
"""

import random

def QuickSort(arr, l, r):
    if l < r:
        pivot = partition_random(arr, l, r)
        
        QuickSort(arr, l, pivot-1)
        QuickSort(arr, pivot+1, r)
        
def partition_random(a, l , r):
    p_random = random.choice(range(l, r+1))
    a[l], a[p_random] = a[p_random], a[l]
    return partition(a, l, r)

def partition(a, l, r):
    p = a[r]
    i = l-1
    
    for j in range(l, r):
        if a[j] <= p:
            i+=1
            a[j], a[i] = a[i], a[j]
    a[i+1], a[r] = a[r], a[i+1]
    return i+1

print('Enter the numbers separated by space')
s = input()
a = list(map(int, s.split()))
QuickSort(a, 0, len(a)-1)