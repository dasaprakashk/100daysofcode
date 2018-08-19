#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 17:18:39 2018

@author: Das
"""

import random

def kthSmallest(a, l, r, k):
    if k>0 and k<= r - l + 1:
        pivot = partition(a, l, r)
        if k-1 == pivot-l:
            return a[pivot]
        if k-1 < pivot-l:
            return kthSmallest(a, l, pivot-1, k)
        else:
            return kthSmallest(a, pivot+1, r, k-pivot+l-1)
    
def partition(a, l, r):
    p_random = random.choice(range(l, r))
    a[p_random], a[r] = a[r], a[p_random]
    pivot = a[r]
    i = l
    for j in range(l, r):
        if a[j] < pivot:
            a[j], a[i] = a[i], a[j]
            i += 1
    a[i], a[r] = a[r], a[i]
    return i


print('Enter numbers separated by space:')
s = input()
arr = list(map(int, s.split()))

kth = kthSmallest(arr, 0, len(arr)-1, 5)
print(kth)