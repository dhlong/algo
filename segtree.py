# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 22:22:20 2020

@author: dhlon
# """


def stree_build(a):
    n = len(a)
    t = [0]*n + a
    for i in reversed(range(n)):
        t[i] = t[i<<1] + t[(i<<1)|1]
    return t


def stree_update(t, p, v):
    n = len(t)//2
    p += n
    t[p] = v
    while p > 1:
        t[p>>1] = t[p] + t[p^1]
        p >>= 1
        
        
def stree_query(t, l, r):
    n = len(t)//2
    l += n
    r += n
    res = 0
    while l < r:
        if l&1:
            res += t[l]
            l += 1
        if r&1:
            r -= 1
            res += t[r]
        l >>= 1
        r >>= 1
    return res


a = [1,2,3,4,5,6,7,8]
t = stree_build(a)
print(stree_query(t, 3, 6))
stree_update(t, 5, 10)
print(stree_query(t, 3, 6))
