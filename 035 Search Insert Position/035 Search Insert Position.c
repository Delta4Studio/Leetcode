int searchInsert(int* nums, int numsSize, int target) {
    if( *(nums) >= target )
        return 0;
    int l = 0, r = numsSize, m = (int) ((l+r)/2+0.5);
    if( target > *(nums+r-1) )
        return r;
    if(target == *(nums+r-1) )
        return r-1;
    while(true){
        if(target <= *(nums+m) && target > *(nums+m-1))
            return m;
        else if(target < *(nums+m))
            r = m;
        else if(target > *(nums+m))
            l = m;
        m = (int) ((l+r)/2+0.5);
    }
}
//Min:4ms