class Solution(object): 
    def singleNumber(self, nums):
        """ 
        :type nums: List[int] 
        :rtype: int 
        """ 
        if ( len(nums) == 1 ): 
            return nums[0] 
        x = 0 
        for i in nums: 
            x ^= i 
        return x 
#Min:48ms