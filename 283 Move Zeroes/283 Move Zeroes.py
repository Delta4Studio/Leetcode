class Solution(object):
    def moveZeroes(self, nums):
        c = 0
        i = 0
        while i < len(nums):
            if nums[i] != 0:
                nums[c] = nums[i]
                c+=1
            i+=1
        for j in range(c, i):
            nums[j] = 0
#64ms