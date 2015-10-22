var moveZeroes = function(nums){
    var i=0, c= nums.length;
    while(i < c)
        if (nums[i] == 0){
            nums.splice(i,1);
            nums.push(0);
        }else{
            i++;
        }
}
//Min:136ms