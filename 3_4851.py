import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

li = []
#li = list()

def insertF(pos, value):
    if pos==1:
        li.append(value)
    else:
        li.insert(0,value)
    print('list: ', li)

def eraseF(pos, value):
    cnt = 0
    if pos == 0:
        for i in range(len(li)):        # range(0,1,2,3,...,len-1) 로 고정, list값을 지우면, i랑 len을 재설정해야하므로 while문 이용필요
            print(i)
            if li[i]>=value:
                del li[i]
                cnt+=1
                if cnt>=3: break

def sortF(value):
    pass

def printF(pos):
    if pos==1:
        #for x in li:
        #    print(x, end=' ')
        #print()
        print(*li)

    else:
        print(*li[::-1])


for _ in range(int(input())):
    #cmd = input().split()
    #cmd = list(map(int, cmd))   # [int(cmd[0]), int(cmd[1]), .. , int(cmd[len-1])]

    cmd = list(map(int, input().split()))
    print('cmd: ', *cmd)
    if cmd[0]==1: insertF(cmd[1], cmd[2])
    elif cmd[0]==2: eraseF(*cmd[1:])
    elif cmd[0]==3: sortF(cmd[1])
    else: printF(cmd[1])