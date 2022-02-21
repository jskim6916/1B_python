import sys
sys.stdin=open('input.txt')
input = sys.stdin.readline

n = int(input())
li = []
for _ in range(n):
    li.append(tuple(map(int, input().split())))
li.sort(key=lambda t : t[2])

ids, cnt, end = [], 0, 0
for id, s, e in li:
    if end <= s:
        cnt+=1
        end = e
        ids.append(id)
print(cnt)
print(*ids)