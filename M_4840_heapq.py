import sys
from collections import defaultdict
from heapq import heappush, heappop

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
maxsum, minsum, maxavg, minavg = [], [], [], []

def push(pid):
    heappush(maxsum, (-P[pid].sum, -pid))
    heappush(maxavg, (-P[pid].avg, -pid))
    heappush(minsum, (P[pid].sum, pid))
    heappush(minavg, (P[pid].avg, pid))

for i in range(1, m+1): push(i)
for _ in range(int(input())):
    cmd = input().split()
    if cmd[0] == 'EVAL':
        sid, pid, score = map(int, cmd[1:])
        if pid in S[sid]: P[pid].update(score-S[sid][pid], 0)
        else: P[pid].update(score, 1)
        S[sid][pid] = score
        push(pid)

    if cmd[0] == 'CLEAR':
        sid = int(cmd[1])
        for pid, score in S[sid].items():
            P[pid].update(-score, -1)
            push(pid)
        S[sid].clear()

    if cmd[0] == 'SUM':
        pq = maxsum if cmd[1]=='1' else minsum
        while abs(pq[0][0]) != P[abs(pq[0][1])].sum: heappop(pq)
        print(abs(pq[0][1]))

    if cmd[0] == 'AVG':
        pq = maxavg if cmd[1]=='1' else minavg
        while abs(pq[0][0]) != P[abs(pq[0][1])].avg: heappop(pq)
        print(abs(pq[0][1]))