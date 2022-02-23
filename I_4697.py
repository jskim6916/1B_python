import sys
import heapq as hq
sys.stdin=open('input.txt')
input=sys.stdin.readline

S = [0] * 100001
maxpq, minpq = [], []

# call by reference : [immutable] list, set, dict , ..
# call by value : numeric , tuple, frozenset

def get(pq):
    while pq and abs(pq[0][0]) != S[abs(pq[0][1])]:
        hq.heappop(pq)
    if pq: print(abs(pq[0][1]))
    else: print(-1)

for _ in range(int(input())):
    cmd = list(map(int,input().split()))
    if cmd[0]==1:
        id, value = cmd[1:]
        S[id] = value
        hq.heappush(minpq, (value, id))
        hq.heappush(maxpq, (-value, -id))
    elif cmd[0]==2:
        S[cmd[1]] = 0
    elif cmd[0]==3: get(minpq)
    else: get(maxpq)

