#!/usr/bin/env python
# -*- coding: utf-8 -*-


print 'hello', 'ssss'
if a > 0:
	print a;
else:
	print -a;
	
"""
age = 30
if age > 18:
    print 'your age is ', age
    print 'adult'
else:
    print 'children'

sum = 0
for i in range(101):
    sum = sum + i
print sum

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print sum

max = 8
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print b
        a, b = b, a + b
        n = n + 1

fib(max)
"""
"""
L=['adam', 'LISA', 'barT','e']

def f(L):
    n = 1
    leng = len(L)
    strings = ''
    for s in L:
        #print 's= ',s
        if isinstance(s,str):
            if(n == 1):
                #print s.upper()
                strings = strings + s.upper()
            else:
                #print 's before lower =', s
                strings = strings + s.lower()
                #print s.lower()
        if (n == leng):
            return strings
        else:
            n = n + 1
            #print 'n=, leng=, ', n, leng

print f('ad22r2R2Am')
print map(f,L)
"""

def not_empty(s):
    return s and s.strip()

print filter(not_empty, ['A', '', 'B', None, 'C', '  '])


str = range(1,101)

def sushu(s):
    flag = 0
    if (s == 1):
        return s
    else:
        for a in range(2,s):
            if (s%a == 0):
                flag = 1
                break
        if (flag == 0):        
            return s
print filter(sushu, str)