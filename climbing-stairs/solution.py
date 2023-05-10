class Solution(object):
    def climbStairs(self, n: int) -> int:
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
          return 1

        hash_memo = {
           0: 1,
           1: 1
        }

        for i in range(2, n+1):
           hash_memo[i] = hash_memo[i-1]+ hash_memo[i-2]

        return hash_memo[n]

solution = Solution()
print(solution.climbStairs(2))
print(solution.climbStairs(38))


"""
return cs(1) + cs(0)

"""