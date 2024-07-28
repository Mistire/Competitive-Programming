class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def convert(num):
            return int(''.join(str(mapping[int(digit)]) for digit in str(num)))

        mapped_nums = [(num, convert(num)) for num in nums]
        mapped_nums.sort(key=lambda x: x[1])
        sorted_nums = [num for num, _ in mapped_nums]
        return sorted_nums