class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1, len_s2 = len(s1), len(s2)
        
        if len_s1 > len_s2:
            return False
        
        counter_s1 = Counter(s1)
        counter_window = Counter(s2[:len_s1])

        for i in range(len_s2 - len_s1):
            if counter_s1 == counter_window:
                return True

            # Update the window by removing the leftmost character and adding the rightmost character
            counter_window[s2[i]] -= 1
            if counter_window[s2[i]] == 0:
                del counter_window[s2[i]]
            counter_window[s2[i + len_s1]] += 1

        return counter_s1 == counter_window