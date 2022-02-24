import sys
sys.stdin=open('input.txt')
input=sys.stdin.readline

P = [0] + [-1] * 10000
C = [set() for _ in range(10001)]

def isParent(x, y):
    while 1:
        if y==x: return 1
        if y==0: return 0
        y=P[y]

def getDistRoot(x):
    dist = 0
    while x != 0:
        dist+=1
        x=P[x]
    return dist

def getDistChild(x):
    dist = 0
    for y in C[x]:
        dist = max(dist, getDistChild(y)+1)
    return dist

def getCnt(x):
    cnt = 1
    for y in C[x]:
        cnt += getCnt(y)
    return cnt

for _ in range(int(input())):
    cmd = input().split()
    if cmd[0]=='add':
        x, y = map(int, cmd[1:])
        P[x] = y
        C[y].add(x)
    elif cmd[0]=='remove':
        x = int(cmd[1])
        if x!=0:
            y = P[x]
            P[x] = -1
            C[y] -= {x}
            C[y] |= C[x]
            for i in C[x]: P[i] = y
    elif cmd[0]=='move':
        x, y = map(int, cmd[1:])
        if P[x] == -1 or P[y] == -1 or x==y: continue
        if isParent(x, y): continue
        C[P[x]] -= {x}
        C[y] |= {x}
        P[x] = y
    else:
        x = int(cmd[1])
        print(getDistRoot(x), getDistChild(x), getCnt(x))
