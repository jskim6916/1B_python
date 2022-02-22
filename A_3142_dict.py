import sys
sys.stdin=open('input.txt')
input = sys.stdin.readline

db = {}
loginCnt = 0

for _ in range(int(input())):
    cmd, id = input().split()
    if cmd=='1':
        print(int(id in db))
    if cmd=='2':
        print(int(id in db and db[id]))
    if cmd=='3':
        if id not in db: db[id] = 0
        print(len(db))
    if cmd=='4':
        if id in db:
            loginCnt -= db[id]
            del db[id]
        print(len(db))
    if cmd=='5':
        if id in db and db[id]==0:
            db[id]=1
            loginCnt+=1
        print(loginCnt)
    if cmd=='6':
        if id in db and db[id]==1:
            db[id]=0
            loginCnt-=1
        print(loginCnt)