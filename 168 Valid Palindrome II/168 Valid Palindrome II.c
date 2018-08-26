bool validPalindrome(char* s) {
    // 取得陣列長度
    int count = strlen(s);
    // 所需變數
    // 指標 : i 為左邊, j 為右邊, k 為所需刪除的字之位置
    int i, j, k=-1;
    
    i = 0;
    j = count-1;
    
    while( i <= j){
        // 如果兩邊文字不同
        if( *(s+i) != *(s+j) ){
            // 確認是否有出現過一次
            if (k != -1){
                // 出現過直接輸出 false
                return false;
            }else{
                // 確認往下的一個數是不是可以對應
                if( *(s+i+1) == *(s+j) ){
                    // 防止例外狀況發生
                    if( *(s+i+2) == *(s+j-1) ){
                        k = i;
                        i++;
                    }else{
                        k = j;
                        j--;
                    }
                }else if( *(s+i) == *(s+j-1) ){
                        k = j;
                        j--;
                // 沒有就直接 false
                }else{
                    return false;
                }
            }
        }
        // 兩邊指標移動
        i++;
        j--;
    }
    // 可以印出需要刪除甚麼字並且顯示在哪個位置
    // printf("You could delete the character \'%c\' in %d", *(s+k), k+1);
    return true;
}
