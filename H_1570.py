import sys, heapq as hq
sys.stdin=open('input.txt')
input=sys.stdin.readline

n, mid = int(input()), int(input())
print(mid)

L, R = [], []
for _ in range(n//2):
    for x in map(int,input().split()):
        hq.heappush(L, -x) if x < mid else hq.heappush(R, x)
    if len(L) > len(R):
        hq.heappush(R, mid)
        mid = -hq.heappop(L)
    elif len(L) < len(R):
        hq.heappush(L, -mid)
        mid = hq.heappop(R)
    print(mid)

