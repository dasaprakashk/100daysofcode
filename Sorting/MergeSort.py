#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 21:31:51 2018

@author: Das
"""

def merge(a, l, m, r):
    lindex = m - l + 1
    rindex = r - m
    p = 0
    q = 0
    k = l
    
    Larray = [0] * (lindex)
    Rarray = [0] * (rindex)
    
    Larray = a[l:l+lindex]
    Rarray = a[m+1: m+rindex+1]
    
    while p < lindex and q < rindex:
        if Larray[p] <= Rarray[q]:
            a[k] = Larray[p]
            p += 1
        else:
            a[k] = Rarray[q]
            q += 1
        k += 1
    while p < lindex:
        a[k] = Larray[p]
        p += 1
        k += 1
    while q < rindex:
        a[k] = Rarray[q]
        q += 1
        k += 1

def MergeSort(a, start, end):
    if start < end:
        mid = (start + (end - 1)) // 2
        MergeSort(a, start, mid)
        MergeSort(a, mid+1, end)
        merge(a, start, mid, end)

print('Enter the elements separated by space')
a = input()


a = a.split(' ')
a = list(map(int, a))

MergeSort(a,0,len(a)-1)
