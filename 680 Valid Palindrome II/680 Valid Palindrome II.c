bool validPalindrome(char* s) {
    // 取得陣列長度
    int count = strlen(s);
    // 所需變數
    // 指標 : i 為左邊, j 為右邊, k 為所需刪除的字之位置
    int i, j, k=-1;
    int i1,j1;
    
    i = 0;
    j = count-1;
    
    while( i < j){
        // 如果兩邊文字不同
        if( *(s+i) != *(s+j) ){
            break;
        }
        // 兩邊指標移動
        i++;
        j--;
    }
    if(i>=j)
        return true;
    
    i1 = i+1;
    j1 = j;
    while( i1 < j1){
        // 如果兩邊文字不同
        if( *(s+i1) != *(s+j1) ){
            break;
        }
        // 兩邊指標移動
        i1++;
        j1--;
    }
    if(i1>=j1)
        return true;
    
    i1 = i;
    j1 = j-1;
    while( i1 < j1){
        // 如果兩邊文字不同
        if( *(s+i1) != *(s+j1) ){
            break;
        }
        // 兩邊指標移動
        i1++;
        j1--;
    }
    if(i1>=j1)
        return true;
    return false;
}

//Min 24ms
