import sys
from collections import defaultdict

sys.stdin=open('input.txt')
input=sys.stdin.readline

class Player:
    sum, avg, cnt = 0, 0, 0
    def update(self, dsum, dcnt):
        self.sum+=dsum
        self.cnt+=dcnt
        self.avg = round(self.sum / self.cnt) if self.cnt else 0

n, m = map(int,input().split())
P = [ Player() for _ in range(m+1)]
S = [ defaultdict(int) for _ in range(n+1)]

for _ in range(int(input())):
    cmd = input().split()
    #print(cmd)
    if cmd[0] == 'EVAL':
        sid, pid, score = map(int, cmd[1:])
        if pid in S[sid]: P[pid].update(score-S[sid][pid], 0)
        else: P[pid].update(score, 1)
        S[sid][pid] = score

    if cmd[0] == 'CLEAR':
        sid = int(cmd[1])
        for pid, score in S[sid].items():
            P[pid].update(-score, -1)
        S[sid].clear()

    if cmd[0] == 'SUM':
        func = max if cmd[1]=='1' else min
        print(func(range(1, m + 1), key=lambda x: (P[x].sum, x)))

    if cmd[0] == 'AVG':
        func = max if cmd[1]=='1' else min
        print(func(range(1, m + 1), key=lambda x: (P[x].avg, x)))