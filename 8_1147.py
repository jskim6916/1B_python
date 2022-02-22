import sys
sys.stdin=open('input.txt')
input = sys.stdin.readline

n = int(input())
dice = [[0 for _ in range(7)] for _ in range(n)]
dice = [[0] * 7 for _ in range(n)]
#dice = [[0] * 7] * n    # list=mutable XXXX reference copy

for i in range(n):
    a,b,c,d,e,f = map(int,input().split())
    for x,y in [(a,f),(b,d),(c,e)]:
        dice[i][x], dice[i][y] = y, x
maxSum = 0
for bottom in range(1, 7):
    sum = 0
    for i in range(n):
        top = dice[i][bottom]
        sum += max(range(1,7), key=lambda x: 0 if x in (bottom, top) else x)
        bottom = top
    maxSum = max(maxSum, sum)
print(maxSum)