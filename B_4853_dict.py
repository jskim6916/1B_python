import sys
sys.stdin=open('input.txt')
input = sys.stdin.readline

prefix = set()
word = {}

for _ in range(int(input())):
    text = input().strip()

    s, ret = '', ''
    for ch in text:
        s+=ch
        if (ret=='') and (s not in prefix):
            ret = s
        prefix.add(s)

    # if text in word: word[text]+=1
    # else: word[text]=1

    word.setdefault(text, 0)
    word[text]+=1

    # if ret=='':
    #     print(text,end='')
    #     if word[text]>1: print(word[text])
    #     else: print()
    # else: print(ret)

    if ret=='':
        ret = text
        if word[text]>1: ret+=str(word[text])
    print(ret)
