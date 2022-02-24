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
        self.avg = round(self.sum / self.cnt, 1) if self.cnt else 0

    def __repr__(self):
        return '{'+str(self.sum)+ ' ' +str(self.avg)+' ' +str(self.cnt)+'}'

class MinPQ:
    def __init__(self,priority, name):
        self.priority = priority
        self.name = name
    def __lt__(self, rhs):       # <
        if self.priority != rhs.priority:
            return self.priority < rhs.priority
        return self.name < rhs.name

class MaxPQ:
    def __init__(self, priority, name):
        self.priority = priority
        self.name = name
    def __lt__(self, rhs):       # <
        if self.priority != rhs.priority:
            return self.priority > rhs.priority
        return self.name > rhs.name

n, m = map(int,input().split())
P = {}
S = defaultdict(dict)
maxsum, minsum, maxavg, minavg = [], [], [], []

def push(pname):
    heappush(maxsum, MaxPQ(P[pname].sum, pname))
    heappush(maxavg, MaxPQ(P[pname].avg, pname))
    heappush(minsum, MinPQ(P[pname].sum, pname))
    heappush(minavg, MinPQ(P[pname].avg, pname))

for name in input().split():
    P[name] = Player()
    push(name)

for _ in range(int(input())):
    cmd = input().split()
    if cmd[0] == 'EVAL':
        sid, pname, score = int(cmd[1]), cmd[2], int(cmd[3])
        if pname in S[sid]: P[pname].update(score-S[sid][pname], 0)
        else: P[pname].update(score, 1)
        S[sid][pname] = score
        push(pname)

    if cmd[0] == 'CLEAR':
        sid = int(cmd[1])
        for pname, score in S[sid].items():
            P[pname].update(-score, -1)
            push(pname)
        S[sid].clear()

    if cmd[0] == 'SUM':
        pq = maxsum if cmd[1]=='1' else minsum
        while pq[0].priority != P[pq[0].name].sum: heappop(pq)
        print(pq[0].name)

    if cmd[0] == 'AVG':
        pq = maxavg if cmd[1]=='1' else minavg
        while pq[0].priority != P[pq[0].name].avg: heappop(pq)
        print(pq[0].name)
