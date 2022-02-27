class Node:
    def __init__(self):
        self.leaf = False
        self.child = {}  # child[다음 문자]=Node

class Trie:
    head = Node()
    def insert(self, word):
        cur = self.head
        for c in word:
            if c not in cur.child:
                cur.child[c] = Node()
            cur = cur.child[c]
        cur.leaf = True

    def search(self, word):
        cur = self.head
        for c in word:
            if c not in cur.child:
                return False
            cur = cur.child[c]
        return True         # 존재하는 prefix인지
        return cur.leaf     # 존재하는 단어인지

trie = Trie()
while True:
    cmd, word = input().split()
    if cmd=='0': trie.insert(word)
    if cmd=='1': print(trie.search(word))