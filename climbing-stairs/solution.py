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
    def climbStairsPointer(self, n: int) -> int:
        """
        :type n: int
        :rtype: int
        """

        if n == 1:
          return 1

        first, second, result = 1, 1, 1
        for _ in range(2, n+1):
           result = first + second
           second = first
           first = result
        return result

solution = Solution()
print(solution.climbStairsPointer(2))
print(solution.climbStairsPointer(38))


"""
return cs(1) + cs(0)

"""