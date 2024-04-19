class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordCount = Counter(words)
        wordTup = [(-frq, word) for word, frq in wordCount.items()]
        wordSm = nsmallest(k, wordTup)
        res = [word for x, word in wordSm]
        return res