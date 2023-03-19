from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l+r) // 2

            if nums[mid] > nums[r]:     # mid - min - r
                l = mid + 1
            else:
                r = mid
        return nums[l]

s=Solution()
print(s.findMin([3,4,5,1,2]))