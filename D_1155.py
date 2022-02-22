import sys
from collections import defaultdict

sys.stdin=open('input.txt')
input=sys.stdin.readline

K, text = int(input()), input().strip()
key = [0,0,0,0]
idx = {'A':0, 'C':1, 'G':2, 'T':3}
idx = dict(zip(['A','C','G','T'],[0,1,2,3]))
idx = dict(zip(*'ACGT'.split(),[0,1,2,3]))
idx = dict(zip(list('ACGT'),[0,1,2,3]))
#print(tuple(zip([1,2,3,4],[5,6,7,8],[9,10,11,12])))

htab = {}
htab = defaultdict(int)

#print('sdfdsfsdf'.find('d'))  # 1
#print('sdfsfsdf'.find('fsf')) # 2
for i in range(len(text)):
    key['ACGT'.find(text[i])]+=1
    if i>=K: key['ACGT'.find(text[i-K])]-=1

    # key[idx[text[i]]]+=1
    # if i >= K: key[idx[text[i-K]]] -= 1

    #htab.setdefault(tuple(key), 0)   #dict인 경우
    if i>=K-1: htab[tuple(key)]+=1

print(max(htab.values()))

