class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_end = True

    def search_prefix(self, word):
        cur = self.root
        prefix = ""

        for c in word:
            if c not in cur.children:
                break
            cur = cur.children[c]
            prefix += c
            if cur.is_end:
                return prefix
        return word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()

        for word in dictionary:
            trie.insert(word)
        
        def replace(word):
            return trie.search_prefix(word)
        sent = sentence.split()

        return ' '.join(replace(word)for word in sent)
        