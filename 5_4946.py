import sys
from heapq import nlargest

sys.stdin=open('input.txt')
input=sys.stdin.readline

D = {}  # D[pid] = [salary, C, J, P]

for _ in range(int(input())):
    cmd = input().split()
    cmd[1:] = map(int, cmd[1:])
    #print(cmd)
    if cmd[0]=='register':
        D[cmd[1]] = cmd[2:]
        #print(cmd[1], D[cmd[1]])

    elif cmd[0]=='cancel':
        if cmd[1] in D: del D[cmd[1]]

    elif cmd[0]=='update':
        pid, flag, X = cmd[1:]
        if pid in D:
            D[pid][flag+1] = X

    elif cmd[0]=='hire_min':
        pid = min(D.items(), key=lambda I : (I[1][0],I[0]))[0]    # (pid, [salary, C, J, P])
        #pid = min(D.keys(), key= lambda pid : (D[pid][0], pid))
        print(pid)
        del D[pid]

    else:
        pids = nlargest(3,D.keys(),key=lambda pid: (sum(D[pid][1:]), pid))
        #items = nlargest(3, D.items(), key=lambda I: (sum(I[1][1:]), I[0]))
        #pids = list(map(lambda I: I[0], items))
        print(*pids)
        for pid in pids: del D[pid]
