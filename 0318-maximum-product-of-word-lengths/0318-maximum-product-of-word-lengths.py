class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        word_int, word_len = [0]*n, [0]*n

        for i in range(n):
            w = words[i]
            len_w = len(words[i])
            w_int = 0
            for j in range(len_w):
                w_int |= 1 << (ord(w[j]) - ord('a'))
            word_int[i] = w_int
            word_len[i] = len_w

        max_p = 0
        for i in range(n-1):
            for j in range(i+1, n):
                if (word_int[i] & word_int[j]) == 0:
                    max_p = max(max_p, (word_len[i] * word_len[j]))
        
        return max_p
