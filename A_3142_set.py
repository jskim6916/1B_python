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
        member.add(id)  #중복허용x
        print(len(member))
    if cmd=='4':
        if id in member: member.remove(id)
        if id in login: login.remove(id)
        print(len(member))
    if cmd=='5':
        if id in member: login.add(id)
        print(len(login))
    if cmd=='6':
        if id in login: login.remove(id)
        print(len(login))