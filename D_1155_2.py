import sys
from collections import defaultdict

sys.stdin=open('input.txt')
input=sys.stdin.readline

K, text = int(input()), input().strip()
key = 0
htab = defaultdict(int)
base = dict(zip(list('ACGT'), [1001**x for x in range(4)]))
base = {'A':1, 'C':1001, 'G':1001**2, 'T':1001**3}

for i in range(len(text)):
    #key += 1001**('ACGT'.find(text[i]))
    #if i>=K: key -= 1001**('ACGT'.find(text[i-K]))

    key += base[text[i]]
    if i>=K: key -= base[text[i-K]]
    if i>=K-1: htab[key]+=1
print(max(htab.values()))

