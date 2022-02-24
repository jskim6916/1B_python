import sys
from collections import deque
sys.stdin=open('input.txt')
input=sys.stdin.readline

#dx, dy = [-1,0,1,0], [0,1,0,-1]
def bfs(sx, sy):
    q = deque([(sx,sy,3)])
    A[sx][sy] = 0
    while q:
        x, y, tick = q.popleft()
        for dx, dy in zip([-1,0,1,0], [0,1,0,-1]):
            nx, ny = x + dx, y + dy
            if nx<0 or nx>=n or ny<0 or ny>=m: continue
            if A[nx][ny]==0: continue
            q.append((nx,ny,tick+1))
            A[nx][ny] = 0
    return tick

m, n = map(int, input().split())
A = [list(map(int,*input().split())) for _ in range(n)]
sy, sx = map(int, input().split())

print(bfs(sx-1, sy-1))
print(sum([sum(A[i]) for i in range(n)]))