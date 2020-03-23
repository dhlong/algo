# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 01:27:39 2020

@author: long
"""

            
# build suffix array + LCP (with kansai method)
def build_sufarr(s):
    n = len(s)
    sa = list(range(n))
    rank = [ord(ch) - ord('a') + 1 for ch in s] + [0]*(1<<n.bit_length())
    rank2 = [0]*len(rank)
    
    for j in range(n.bit_length()):
        k = 1<<j
        sa.sort(key = lambda i: (rank[i], rank[i+k]))
        
        r = 0
        for i in range(n):
            if i==0 or rank[sa[i]] != rank[sa[i-1]] or rank[sa[i]+k] != rank[sa[i-1]+k]:
                r += 1
            rank2[sa[i]] = r
            
        rank, rank2 = rank2, rank
        
    # kansai
    k = 0
    lcp = [0]*n
    s += '$'
    
    for i in range(n):
        if rank[i] < n:
            while s[i+k] == s[sa[rank[i]]+k]:
                k += 1
            lcp[rank[i]-1] = k
        k -= (k>0)

    return sa, lcp


# build LCP from suffix array and original string
def kansai(s, sufArr):
    n = len(s)
    invSuf = [-1]*n
    lcp = [0]*n
    
    for i, suf in enumerate(sufArr):
        invSuf[suf] = i
    
    k = 0
    for i in range(n):
        if invSuf[i] == n-1:
            k = 0
            continue
        
        j = sufArr[invSuf[i] + 1]
        while i+k < n and j+k < n and s[i+k] == s[j+k]:
            k += 1
            
        lcp[invSuf[i]] = k
        
        if k>0:
            k -= 1
            
    return lcp



# incomplete
def build_suffixes_radix(s):
    n = len(s)
    sa = list(range(n))
    sa2 = [0]*n
    rank = [ord(ch) - ord('a') + 1 for ch in s] + [0]*(1<<n.bit_length())
    cnt = [0]*n
    for i in range(n):
        cnt[rank[i]] += 1
    for i in range(1, max(rank)):
        cnt[i] += cnt[i-1]
    for i in range(n):
        cnt[rank[i]] -= 1
        sa[cnt[rank[i]]] = i
    
    
    for j in range(n.bit_length()):
        k = 1<<j
        for i in range(n):
            sa2[i] = sa[i] - k
            if sa2[i] < 0:
                sa2[i] += n
        cnt = [0]*n
        for i in range(n):
            cnt[rank[sa2[i]]] += 1
        for i in range(1, max(rank)):
            cnt[i] += cnt[i-1]
        for i in reversed(range(n)):
            cnt[rank[sa2[i]]] -= 1
            sa[cnt[rank[sa2[i]]]] = sa2[i]
            
        cnt[sa[0]] = 0
        r = 0
        for i in range(n):
            if i==0 or rank[sa[i]] != rank[sa[i-1]] or rank[sa[i]+k] != rank[sa[i-1]+k]:
                r += 1
            rank2[sa[i]] = r
            
        rank, rank2 = rank2, rank
        
    k = 0
    lcp = [0]*n
    s += '$'
    
    for i in range(n):
        if rank[i] < n:
            while s[i+k] == s[sa[rank[i]]+k]:
                k += 1
            lcp[rank[i]-1] = k
        k -= (k>0)

    return sa, lcp

# test    
s = 'banana'
sa, lcp = build_sufarr(s)
lcp2 = kansai(s, sa)
print(sa)
print(lcp)
print(lcp2)