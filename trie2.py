class Node:
    def __init__(self):
        self.leaf = False
        self.child = {}  # child[다음 문자]=Node

def insert(word):
    cur = trie
    for c in word:
        if c not in cur.child:
            cur.child[c] = Node()
        cur = cur.child[c]
    cur.leaf = True

def search(word):
    cur = trie
    for c in word:
        if c not in cur.child:
            return False
        cur = cur.child[c]
    return True         # 존재하는 prefix인지
    return cur.leaf     # 존재하는 단어인지

trie = Node()

while True:
    cmd, word = input().split()
    if cmd=='0': insert(word)
    if cmd=='1': print(search(word))