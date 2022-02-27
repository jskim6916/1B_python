import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

idcnt = 0
class Node:
    def __init__(self):
        self.leaf = False
        self.child = {}
        self.id = 0
        self.score = 0

class Trie:
    head=Node()
    def insert(self, word, score):
        #print(word,score)
        global idcnt
        cur = self.head
        for c in word:
            if c not in cur.child:
                cur.child[c] = Node()
            cur = cur.child[c]
        if cur.leaf==False:
            cur.leaf = True
            idcnt+=1
            cur.id = idcnt
            cur.score = score

        else:
            cur.score = max(cur.score, score)
        print(cur.id, cur.score)

trie = Trie()

for _ in range(int(input())):
    word, score = input().split()
    trie.insert(word.lower(), int(score))

