import sys
from collections import defaultdict
from heapq import heappush, heappop

sys.stdin=open('input.txt')
input=sys.stdin.readline

C = defaultdict(int)
minpq, maxpq = [], []

def sell(pq):
    while abs(pq[0]) not in C: heappop(pq)
    x = abs(heappop(pq))
    C[x]-=1
    print(x, C[x])
    if C[x]==0: del C[x]

for _ in range(int(input())):
    cmd,x = map(int, input().split())
    #print(cmd,x)
    if cmd==1:
        C[x]+=1
        heappush(minpq, x)
        heappush(maxpq, -x)
        print(C[x])
    elif cmd==2:
        if x not in C: print(-1)
        else:
            C[x]-=1
            print(C[x])
            if C[x]==0: del C[x]
    else:
        sell(maxpq if x else minpq)