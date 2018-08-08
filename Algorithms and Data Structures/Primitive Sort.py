#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 10:19:20 2018

@author: Das
"""

'''
1st input number of elements
2nd input - array of elements to be be sorted
'''

def insertion_sort(a):
    for i in range(len(a) - 1):
        for j in range(i+1, len(a)):
            if a[i] > a[j]:
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
        for k in range(len(a)):
            print(a[k], end =" ")
        print('')
        
def selection_sort(a):
    for i in range(len(a)-1):
        idx = i
        for j in range(i+1, len(a)):            
            if a[j] < a[idx]:
                idx = j
        temp = a[i]
        a[i] = a[idx]
        a[idx] = temp
        for k in range(len(a)):
            print(a[k], end =" ")
        print('')
        
def bubble_sort(a):
    swapped = True
    while swapped:
        swapped=False
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp
                swapped = True
        for k in range(len(a)):
            print(a[k], end =" ")
        print('')
        
print('Enter the elements separated by space')
a = input()


a = a.split(' ')
a1 = list(map(int, a))
a2 = list(map(int, a))
a3 = list(map(int, a))
print('----Insertion Sort----')
insertion_sort(a1)
print('----Selection Sort----')
selection_sort(a2)
print('----Bubble Sort----')
bubble_sort(a3)