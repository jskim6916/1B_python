import sys
sys.stdin=open('input.txt')
input=sys.stdin.readline

n, m = map(int,input().split())
dice = [1] * (n+1)
used = [0] * 7

def recur(x):
    # base condition
    if x>n:
        print(*dice[1:])
        return

    # normal condition
    st = dice[x-1] if m==2 else 1
    for i in range(st, 7):
        #if i in dice[1:x]: continue        # O(n)
        if m==3 and used[i]: continue       # O(1)
        dice[x] = i
        used[i] = 1
        recur(x+1)
        used[i] = 0

recur(1)