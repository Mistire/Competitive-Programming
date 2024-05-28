class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
            cur.count += 1

    def search(self, word):
        cur = self.root
        tot = 0
        for ch in word:
            cur = cur.children[ch]
            tot += cur.count
        return tot

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        res = []
        for word in words:
            res.append(trie.search(word))
        return res
            

