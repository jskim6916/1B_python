import sys
sys.stdin=open('input.txt')
input = sys.stdin.readline

q = int(input())
D = {}          # key:value     D[word] = [id, score] , D {word:[id,score] , word2:[id2, score2]}
#D = dict()
id = 0

for _ in range(q):
    cmd = input().split()      # black character 기준 분류, list 등록
    word = cmd[0].lower()
    score = int(cmd[1])
    if word not in D:
        id+=1
        D[word] = [id, score]
    else:
        D[word][1] = max(D[word][1], score)

    print(D[word][0], D[word][1])
