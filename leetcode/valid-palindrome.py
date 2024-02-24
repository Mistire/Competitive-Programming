class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        l, r = 0, len(strs) - 1
        while l < r:
            if strs[l] != strs[r]:
               return False
            l += 1
            r -= 1
        return True
        
        