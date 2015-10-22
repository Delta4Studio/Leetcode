void moveZeroes(int *nums, int mumsSize){
    int i, j;
    for(i = 0, j = 0; i<numsSize; i++)
        if(*(nums+i)!=0){
            *(nums+j) = *(nums+i);
            j++;
        }
    for(; j < numsSize; j++)
        *(nums+j) = 0
}
//8ms