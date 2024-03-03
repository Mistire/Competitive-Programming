class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # vowels = set("aeiou")
        # maxVowels = 0
        # curVowels = 0
        
        # for i in range(k):
        #     if s[i] in vowels:
        #         curVowels += 1
        # maxVowels = curVowels
        
        # for i in range(k, len(s)):
        #     if s[i] in vowels:
        #         curVowels += 1
        #     if s[i - k] in vowels:
        #         curVowels -= 1
        #     maxVowels = max(maxVowels, curVowels)
        # return maxVowels

        maxVow = 0
        curVow = 0
        vowels = set("aioue")

        for i in range(k):
            if s[i] in vowels:
                curVow += 1
        maxVow = curVow

        for i in range(k, len(s)):
            if s[i] in vowels:
                curVow += 1
            if s[i-k] in vowels:
                curVow -= 1
            maxVow = max(curVow, maxVow)
        return maxVow




                




