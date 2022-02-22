import sys
sys.stdin=open('input.txt')
input=sys.stdin.readline

n, k = int(input()), int(input())
li = sorted([int(input()) for _ in range(n)])

total, sum = 0, 0
for i in range(k):
    total += li[i] * i - sum
    sum += li[i]
mintotal = total
for i in range(k, n):
    sum-=li[i-k]
    total += (li[i]+li[i-k])*(k-1) - sum * 2
    sum+=li[i]
    mintotal = min(mintotal, total)
print(mintotal)