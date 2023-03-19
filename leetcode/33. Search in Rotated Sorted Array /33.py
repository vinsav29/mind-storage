from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    # left has the  t
                    r = mid - 1
                else:
                    # right has the t
                    l = mid + 1

            else:
                if nums[mid] < target <= nums[r]:
                    # right has the t
                    l = mid + 1
                else:
                    # left has the  t
                    r = mid - 1

        return -1

s=Solution()
print(s.search(nums = [3,1], target = 1))