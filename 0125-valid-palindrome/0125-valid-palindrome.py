class Solution:
    def isPalindrome(self, s: str) -> bool:
        pattern = r'[\W\s_]+'
        s_arr = re.split(pattern, s)
        pal = ''.join(s_arr).lower()
        return (pal == pal[::-1])
        
        
