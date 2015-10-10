int** generate(int numRows, int** columnSizes, int* returnSize) {

    *returnSize = numRows;
    int **p, i, j;

    //設定X軸記憶體
    p = (int**) malloc( numRows * sizeof(int*) );
    *columnSizes = (int*) malloc( numRows * sizeof(int) );
    for( i = 0 ; i < numRows ; i++){
        //設定Y軸記憶體
        p[i] = (int*) malloc( (i + 1) * sizeof(int) );
        p[i][0] = p[i][i] = 1;
        (*columnSizes)[i] = i+1;
        if (numRows >= 2){
            for(j = 1 ; j < i ; j++){
                //設定Y軸各值
                p[i][j] = p[i-1][j-1] + p[i-1][j];
            }
        }
    }
    return p;
}
//Min:0ms
