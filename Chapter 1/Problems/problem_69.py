#  69- Sqrt(x)

# 1st Method

import math
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(math.sqrt(x))
    
solution = Solution()
result = solution.mySqrt(8)

print(result)

# 2nd Method

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        
        left = 1
        right = x
        
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
                
        return right
    
solution = Solution()
result = solution.mySqrt(8)

print(result)


        
        