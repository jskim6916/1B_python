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
    #print('list: ', li)

def eraseF(pos, value):
    cnt = 0
    if pos == 0:
        i = 0
        while i < len(li):
            if li[i]>=value:
                del li[i]
                cnt+=1
                if cnt>=3: break
            else:
                i+=1

    else:
        i = len(li) - 1
        while i>=0 and cnt<3:
            if li[i]>=value:
                del li[i]
                cnt+=1
            i-=1

    #print('list: ', li)

def sortF(value):
    li.sort(key=lambda x : (abs(value-x), x))   # <
    #print(li)

def printF(pos):
    if pos==0:
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
    #print('cmd: ', *cmd)
    if cmd[0]==1: insertF(cmd[1], cmd[2])
    elif cmd[0]==2: eraseF(*cmd[1:])
    elif cmd[0]==3: sortF(cmd[1])
    else: printF(cmd[1])
