import sys

sys.stdin=open('input.txt')
input = sys.stdin.readline

L, R = [], []

for _ in range(int(input())):
    log = input().strip()
    L.clear()
    R.clear()
    for ch in log:
        if ch=='<':
            if len(L): R.append(L.pop())

        elif ch == '>':
            if len(R): L.append(R.pop())

        elif ch == '-':
            if len(L): L.pop()

        else:
            L.append(ch)

    print(''.join(L + R[::-1]))
