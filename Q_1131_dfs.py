#dfs
import sys
sys.stdin=open('input.txt')
input=sys.stdin.readline

dx, dy = [-1,0,1,0], [0,1,0,-1]

def dfs(x,y):
    visited[x][y]=1
    cnt=1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=m: continue
        if A[nx][ny]=='.' or visited[nx][ny]: continue
        cnt += dfs(nx,ny)
    return cnt



m, n = map(int, input().split())
A = [ input().strip() for _ in range(n) ]
visited = [[0]*m for _ in range(n)]
ret = 0
for i in range(n):
    for j in range(m):
        if A[i][j]=='*' and visited[i][j]==0:
            ret = max(ret, dfs(i,j))
print(ret)