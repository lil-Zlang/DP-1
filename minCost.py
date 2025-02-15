class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # costs[i][j] -> i is house, j is color

        dp = [0, 0, 0]

        for i in range(len(costs)):
            dp0 = costs[i][0] + min(dp[1], dp[2])
            dp1 = costs[i][1] + min(dp[0], dp[2])
            dp2 = costs[i][2] + min(dp[0], dp[1])
            dp = [dp0, dp1, dp2]

        return min(dp)


# time complexity: O(n) because we only need to iterate through the costs array once
# space complexity: O(1) because we are only using a constant amount of extra space
