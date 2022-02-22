import sys
sys.stdin=open('input.txt')
input = sys.stdin.readline

member, login = set(), set()

for _ in range(int(input())):
    cmd, id = input().split()
    if cmd=='1':
        print(int(id in member))
    if cmd=='2':
        print(int(id in login))
    if cmd=='3':
        member |= {id}
        print(len(member))
    if cmd=='4':
        member -= {id}
        login -= {id}
        print(len(member))
    if cmd=='5':
        if id in member: login |= {id}
        print(len(login))
    if cmd=='6':
        login -= {id}
        print(len(login))