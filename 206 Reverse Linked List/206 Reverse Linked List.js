var reverseList = function(head){
    var cp = head, np = null, pp;
    while(cp!=null){
        //獲取下一個node
        pp = cp.next;
        
        //設定當前node的下一個對應node為上一個
        cp.next = np;
        
        //指標切換
        np = cp;
        cp = pp;
    }
    return np;
}
//Min:132ms