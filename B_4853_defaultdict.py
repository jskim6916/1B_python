import sys
from collections import defaultdict

sys.stdin=open('input.txt')
input = sys.stdin.readline

prefix = set()
word = defaultdict(int)

for _ in range(int(input())):
    text = input().strip()

    s, ret = '', ''
    for ch in text:
        s+=ch
        if (ret=='') and (s not in prefix):
            ret = s
        prefix.add(s)

    word[text]+=1

    if ret=='':
        ret = text
        if word[text]>1: ret+=str(word[text])
    print(ret)
