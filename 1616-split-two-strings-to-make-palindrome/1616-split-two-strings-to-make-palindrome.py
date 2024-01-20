class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def isPalindrome(s,l,r):
            while l < r and s[l] == s[r]:
                l += 1 ; r -= 1
            return l >= r
        def check(a,b):
            l = 0; r =len(a) - 1
            while l < r and a[l] == b[r]:
                l += 1; r -= 1
            return isPalindrome(a,l,r) or isPalindrome(b,l,r)
        return check(a,b) or check(b,a)