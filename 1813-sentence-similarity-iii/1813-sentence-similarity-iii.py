class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1 = sentence1.split()
        words2 = sentence2.split()
        
        # Ensure words1 is the longer sentence (if not, swap them)
        if len(words1) < len(words2):
            words1, words2 = words2, words1
        
        # Try matching the prefix (words at the start) and suffix (words at the end)
        i, j = 0, 0
        
        # Match prefix
        while i < len(words2) and words1[i] == words2[i]:
            i += 1
        
        # Match suffix
        while j < len(words2) - i and words1[-(j + 1)] == words2[-(j + 1)]:
            j += 1
        
        # If all words in sentence2 are either in the prefix or suffix of sentence1
        return i + j == len(words2)