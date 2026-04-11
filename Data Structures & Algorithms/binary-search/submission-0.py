class Solution:
    def search(self, nums: List[int], target: int) -> int:

        s, e = 0,len(nums)

        while s < e:
            m = (s + e) // 2

            if nums[m] == target:
                return m

            if target < nums[m]:
                e = m

            else:
                s = m + 1

        return -1

        