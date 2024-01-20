class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        count = [0] * 2055
        for start, end in logs:
            for c in range(start,end):
                count[c] += 1
        m = max(count)
        for index in range(len(count)):
            if count[index] == m:
                return index
        return -1