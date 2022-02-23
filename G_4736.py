import sys
#from heapq import nsmallest
import heapq as hq

sys.stdin=open('input.txt')
input=sys.stdin.readline

for _ in range(int(input())):
    A = set()
    for _ in range(int(input())):
        cmd = input().split()
        cmd[1:] = map(int, cmd[1:])
        if cmd[0]=='insert': A.add(cmd[1])  # A|={cmd[1]}
        elif cmd[0]=='erase': A-={cmd[1]}
        elif cmd[0]=='update':
            if cmd[1] in A and cmd[2] not in A:
                A -= {cmd[1]}
                A |= {cmd[2]}
        elif cmd[0]=='front':
            if len(A) == 0: print('empty')
            else:
                #if len(A) < cmd[1]: cmd[1]=len(A)
                #print(hq.nsmallest(cmd[1], A)[cmd[1]-1])
                print(hq.nsmallest(cmd[1], A)[-1])
        else:
            if len(A) == 0: print('empty')
            else: print(hq.nlargest(cmd[1], A)[-1])