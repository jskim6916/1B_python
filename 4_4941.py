import sys
sys.stdin=open('input.txt')
input = sys.stdin.readline

li = []

for _ in range(int(input())):
    cmd, val = input().split()
    #print(cmd, val)
    if cmd=='1': li.append(val.lower())
    elif cmd=='2':
        if val=='0': li.sort()
        elif val=='1': li.sort(reverse=True)
        else: li.sort(key=lambda x: (len(x), x))
        print(*li[:3])
    else:
        li[0] = (li[0]+val.lower())[:15]
        print(li[0])