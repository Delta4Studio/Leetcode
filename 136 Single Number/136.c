int singleNumber(int* nums, int numsSize) { 
    //若遇只有單個數的陣列直接return    
    if(numsSize == 1){ 
        return *nums; 
    } 
    int i, x = 0; 
    for(i = 0; i< numsSize; i++ ){ 
        //作XOR運算
        x ^= *(nums+i); 
    } 
    return x; 
} 
//Min:8ms