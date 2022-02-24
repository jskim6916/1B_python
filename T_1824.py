import sys
sys.stdin=open('input.txt')
input=sys.stdin.readline

sdoku = [ list(map(int,input().split())) for i in range(9) ]
zero = []
row = [[0] * 10 for _ in range(9)]  # row[x][i] = 1/0
col = [[0] * 10 for _ in range(9)]  # col[y][i] = 1/0
grp = [[[0] * 10 for _ in range(3)] for _ in range(3)]  # grp[X][Y][i] = 1/0

for i in range(9):
    for j in range(9):
        if sdoku[i][j] == 0: zero.append((i,j))
        else:
            row[i][sdoku[i][j]] = 1
            col[j][sdoku[i][j]] = 1
            grp[i//3][j//3][sdoku[i][j]]=1


def dfs(c):
    if c == len(zero):
        for i in range(9): print(*sdoku[i])
        return 1

    x,y = zero[c]
    for i in range(1,10):
        if row[x][i] or col[y][i] or grp[x//3][y//3][i]: continue

        sdoku[x][y] = i
        row[x][i], col[y][i], grp[x//3][y//3][i] = 1,1,1
        if dfs(c+1) == 1: return 1
        row[x][i], col[y][i], grp[x//3][y//3][i] = 0,0,0

    return 0

dfs(0)
