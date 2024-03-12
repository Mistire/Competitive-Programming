class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()

        left = 0
        total = 0
        right = len(skill) - 1
        sumF = skill[left] + skill[right]

        while left < right:
            if skill[left] + skill[right] == sumF:
                total += skill[left] * skill[right]
                left += 1
                right -= 1
            elif len(skill) == 2:
                return skill[left] * skill[right]
            else:
                return - 1
        return total
        