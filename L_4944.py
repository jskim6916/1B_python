import sys
from collections import defaultdict
from heapq import heappush, heappop

sys.stdin=open('input.txt')
input=sys.stdin.readline

C = defaultdict(int)
minpq, maxpq = [], []

for _ in range(int(input())):
    cmd,x,cnt = map(int, input().split())

    if cmd==1:
        C[x]+=cnt
        print(C[x])
        heappush(maxpq, -x)
        heappush(minpq, x)

    elif cmd==2:
        C[x]-=cnt
        print(max(0,C[x]))
        if C[x]<=0: del C[x]

    else:
        total = 0
        pq = maxpq if x else minpq
        while pq and cnt:
            if abs(pq[0]) not in C:
                heappop(pq)
                continue
            worth = abs(pq[0])
            sellCnt = min(cnt, C[worth])
            cnt -= sellCnt
            C[worth] -= sellCnt
            total += worth * sellCnt
            if C[worth]==0: del C[worth]
        print(total)