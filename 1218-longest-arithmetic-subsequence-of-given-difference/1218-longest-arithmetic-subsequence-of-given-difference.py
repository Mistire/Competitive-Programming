class Solution:
    def longestSubsequence(self, arr: List[int], diff: int) -> int:
        dp = defaultdict(int)
        res = 0

        for num in arr:
            dp[num] = dp[num-diff] + 1
            res = max(res, dp[num])

        return res

