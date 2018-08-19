#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 20:57:12 2018

@author: Das
"""

import sys

def BinarySearch(a, l, r, k):
    if l < r:
        mid = (l + r - 1) // 2
        if k == a[mid]:
            return mid
        if k < a[mid]:
            return BinarySearch(a, l, mid-1, k)
        else:
            return BinarySearch(a, mid+1, r, k)
    return sys.maxsize

print('Enter sorted list separated by space')
s = input()
a = list(map(int, s.split()))

out = BinarySearch(a, 0, len(a)-1, 0)