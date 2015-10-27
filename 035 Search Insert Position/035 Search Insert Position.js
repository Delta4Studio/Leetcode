var searchInsert = function(nums, target){
    if(nums[0] >= target)
        return 0;
    var l=0, r=nums.length, m=parseInt((l+r)/2+0.5);
    if(target > nums[r-1])
        return r
    if(target === nums[r-1])
        return r-1;
    while(true){
        if(target <= nums[m] && target > nums[m-1])
            return m;
        else if(target < nums[m])
            r = m;
        else if(target > nums[m])
            l = m;
        m = parseInt((l+r)/2+0.5);
    }
};
//112ms