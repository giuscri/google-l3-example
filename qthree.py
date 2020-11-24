class Solution:
    def f(self, A: List[int]) -> int:
        n = len(A)
        dp = [0 for _ in range(n+5)]
        dp[n-1] = A[n-1]
        for i in range(n-2, -1, -1):
            M = A[i] + min(dp[i+2], dp[i+3], dp[i+4])
            if i+1 < len(A):
                M = max(M, A[i]+A[i+1] + min(dp[i+3], dp[i+4], dp[i+5]))
            if i+2 < len(A):
                M = max(M, A[i]+A[i+1]+A[i+2] + min(dp[i+4], dp[i+5], dp[i+6]))
        
            dp[i] = M
        
        return dp[0]
        
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        ascore = self.f(stoneValue)
        if sum(stoneValue)%2 == 0 and ascore == sum(stoneValue)//2:
            return "Tie"
        elif ascore > sum(stoneValue)/2:
            return "Alice"
        else:
            return "Bob"
