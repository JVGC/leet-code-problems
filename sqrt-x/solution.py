class Solution(object):
    def mySqrt(self, x: int) -> int:
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
           return 0
        start = 1
        end = x
        while start <= end:
          mid = start + (end-start)//2
          if mid * mid == x:
            return mid
          elif mid * mid > x:
            end = mid -1
          else:
            start = mid +1
        return end

solution = Solution()

print(solution.mySqrt(4))
print(solution.mySqrt(25))




