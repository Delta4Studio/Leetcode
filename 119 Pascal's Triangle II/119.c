int* getRow(int rowIndex, int* returnSize）{ 
    int i, *p; 
    long long int tmp; 
    
    //修正 
    rowIndex++; 
    //宣告陣列所需記憶體 
    p = (int*) malloc(rowIndex * sizeof(int)); 
    *p = 1; 
    *(p+rowIndex-1) = 1; 
    tmp = 1; 
    
    for( i = 0 ; i < rowIndex ; i++ ){ 
        tmp = tmp * ( rowIndex - i ) / i ; 
        *(p+i) = tmp; 
    } 
    return p; 
}
//Min:0ms