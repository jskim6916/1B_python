import sys
sys.stdin=open('input.txt')
input=sys.stdin.readline

n, q= map(int,input().split())
htab = {}
cnt = [0]*4

for i in range(q):
    pid = i % 4
    key = tuple(map(int,input().split()))

    if key in htab:
        oid = htab[key]
        if pid == oid:
            cnt[pid]-=1
            del htab[key]
        elif cnt[pid] < cnt[oid]:
            htab[key] = pid
            cnt[pid]+=1
            cnt[oid]-=1
    else:
        htab[key] = pid
        cnt[pid]+=1

for c in cnt: print(c)
#print('\n'.join(map(str,cnt)))