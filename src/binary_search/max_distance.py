from typing import List


class Solution:
   # [1,2,3,4,7]
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()

        def count(d):
            ans, curr = 1, position[0]
            for i in range(1, n):
                if position[i] - curr >= d:
                    ans += 1
                    curr = position[i]
            return ans
        
        l, r = 0, position[-1] - position[0]
        while l < r:
            mid = r - ((r-l) // 2)
            if count(mid) >= m:
                l = mid
            else:
                r = mid - 1
        return l

sol = Solution()
ans = sol.maxDistance([1,2,3,4,7], 3)
assert ans == 3