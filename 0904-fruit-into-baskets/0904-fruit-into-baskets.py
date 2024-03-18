class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruCount = defaultdict(int)
        left = 0
        count = 0

        for right in range(len(fruits)):

            fruCount[fruits[right]] += 1
            while len(fruCount) > 2 and left < len(fruits):
                fruCount[fruits[left]] -= 1
                if fruCount[fruits[left]] == 0:
                    del fruCount[fruits[left]]
                left += 1
                
            count = max(right-left+1, count)

        return count 
