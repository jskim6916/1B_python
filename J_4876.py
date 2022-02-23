import sys
import heapq as hq
sys.stdin=open('input.txt')
input=sys.stdin.readline

S = [0] * 100001
maxpq, minpq = [], []

# call by reference : [immutable] list, set, dict , ..
# call by value : numeric , tuple, frozenset

def get(pq):
    ''' 유효한값 3개 찾기 '''
    valid = []
    while pq and len(valid) < 3:
        score, id = hq.heappop(pq)
        if abs(score) != S[abs(id)]: continue
        if valid and valid[-1] == (score, id): continue
        valid.append((score, id))
        #valid += [(score, id)]

    if len(valid) < 3: print(-1)
    else: print(abs(valid[2][1]))

    ''' 유효한값 다시 push '''
    for x in valid:
        hq.heappush(pq, x)

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

