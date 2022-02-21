import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline

dq = deque()

def insertF(pos, value):
    if pos==1:
        dq.append(value)
    else:
        dq.appendleft(value)
    #print('list: ', li)

def eraseF(pos, value):
    cnt = 0
    if pos == 0:
        i = 0
        while i < len(dq):
            if dq[i]>=value:
                del dq[i]
                cnt+=1
                if cnt>=3: break
            else:
                i+=1

    else:
        i = len(dq) - 1
        while i>=0 and cnt<3:
            if dq[i]>=value:
                del dq[i]
                cnt+=1
            i-=1

    #print('list: ', li)

def sortF(value):
    global dq
    dq = deque(sorted(dq, key=lambda x : (abs(value-x), x)))
    # value=3
    # 3 => (0,3)
    # 2 => (1,2)
    # 2 => (1,2)
    # 4 => (1,4)
    # 1 => (2,1)
    # 1 => (2,1)
    #print(dq)

def printF(pos):
    if pos==0:
        #for x in dq:
        #    print(x, end=' ')
        #print()
        print(*dq)

    else:
        print(*reversed(dq))


for _ in range(int(input())):
    #cmd = input().split()
    #cmd = list(map(int, cmd))   # [int(cmd[0]), int(cmd[1]), .. , int(cmd[len-1])]

    cmd = list(map(int, input().split()))
    #print('cmd: ', *cmd)
    if cmd[0]==1: insertF(cmd[1], cmd[2])
    elif cmd[0]==2: eraseF(*cmd[1:])
    elif cmd[0]==3: sortF(cmd[1])
    else: printF(cmd[1])