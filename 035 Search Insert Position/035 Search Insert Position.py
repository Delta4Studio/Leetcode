class Solution(object):
    def searchInsert(self, nums, target):
        if target <= nums[0]:
            return 0
        l = 0
        r = len(nums)
        m = Int((l+r)/2)
        if target > nums[r-1]:
            return r
        elif target == nums[r-1]:
            return r-1
        while True :
            if nums[m] >= target and nums[m-1] < target:
                return m
            elif nums[m] > target:
                r = m
            elif nums[m] < target:
                l = m
            m = Int((l+r)/2+0.5)
#Min:36ms