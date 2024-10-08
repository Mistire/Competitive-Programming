class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False
        s1_count = Counter(s1)
        s2_count = Counter(s2[:n1])

        if s1_count == s2_count:
            return True

        left = 1
        right = n1

        while right < n2:
            s2_count[s2[left-1]] -= 1
            s2_count[s2[right]] += 1
            if s1_count == s2_count:
                return True
            left += 1
            right += 1
        return False