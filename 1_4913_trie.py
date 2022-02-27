import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

cnt = 0

class Node:
    def __init__(self):
        self.leaf = False
        self.child = {}

class Trie:
    head=Node()
    def insert(self, word):
        global cnt
        cur = self.head
        for c in word:
            if c not in cur.child:
                cur.child[c] = Node()
            cur = cur.child[c]
        if cur.leaf==False:
            cur.leaf = True
            cnt+=1
        else:
            cur.leaf = False
            cnt-=1

trie = Trie()
for _ in range(int(input())):
    trie.insert(input().strip())
print(cnt)