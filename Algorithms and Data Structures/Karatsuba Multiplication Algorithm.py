#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 15:22:11 2018

@author: Das
"""

def karatsuba(n1, n2):
    print(n1, n2)
    if len(str(n1))==1 and len(str(n2)) == 1:
        return n1 * n2
    else:
        m = max(len(str(n1)), len(str(n2)))
        m2 = m//2
        
        high1 = n1 // 10**m2
        low1 = n1 % 10**m2
        high2 = n2 // 10**m2
        low2 = n2 % 10**m2
        
        z0 = karatsuba(low1, low2)
        z1 = karatsuba((high1 + low1), (high2 + low2))
        z2 = karatsuba(high1, high2)
        
        return (z2 * 10 ** (m2*2)) + ((z1 - z2 - z0) * 10  ** m2) + z0

n1 = 5678
n2 = 1234
#n1 = 3141592653589793238462643383279502884197169399375105820974944592
#n2 = 2718281828459045235360287471352662497757247093699959574966967627
result = karatsuba(n1, n2)