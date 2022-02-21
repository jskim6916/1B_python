import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

q = int(input())

#dictionary
#D = {}
#D = dict()

S = set()

#list
#L = []
#L = list()

for i in range(q):
    # text = '  jsdifjdsiofj\n'
    # stext.split() => 'jsdifjdsiofj'
    word = input().strip()
    #print(word)
    #print(word, end=': ')
    if word in S:
        S.remove(word)
    elif word not in S:     #else
        S.add(word)
    #print(S)

print(len(S))