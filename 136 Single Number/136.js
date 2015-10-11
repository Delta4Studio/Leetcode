/**
 * @param {number[]} nums
 * @return {number} 
 */ 
var singleNumber = function(nums) { 
    if(nums.length == 1){ 
        return nums[0]; 
    } 
    var x=0; 
    for(var i = 0; i < nums.length ; i++){ 
        x = x ^ nums[i]; 
    } 
    return x; 
}; 
//Min:116ms