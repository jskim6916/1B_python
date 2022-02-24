import sys
from collections import deque

sys.stdin=open('input.txt')
input=sys.stdin.readline

n, m = map(int,input().split())
code = [''] + [ input().strip() for _ in range(n)]
adj = [[] for _ in range(n+1)]
visited = [0] * (n+1)
prev = [0] * (n+1)

def isHamming(a, b):
    dist = 0
    for i in range(m):
        if a[i]!=b[i]: dist+=1
    return dist==1

def traceback(x):
    if x == 0: return
    traceback(prev[x])
    print(x, end=' ')

def bfs():
    s, e = map(int, input().split())
    q = deque([s])
    visited[s] = 1
    while q:
        x = q.popleft()
        for y in adj[x]:
            if visited[y] == 0:
                visited[y] = 1
                q.append(y)
                prev[y] = x
                if y == e:
                    traceback(y)
                    return
    print(-1)

for i in range(1,n+1):
    for j in range(1, i):
        if sum([1 if code[i][k]!=code[j][k] else 0 for k in range(m)]) == 1:
        #if isHamming(code[i], code[j]):
            adj[i].append(j)
            adj[j].append(i)

bfs()