var mergeTwoLists = function(l1, l2){
    var x = new ListNode(0), p = x;
    while(l1||l2){
        if(!l2){
            p.next = l1;
            break;
        }else if(!l1){
            p.next = l2;
            break;
        }else if(l1.val > l2.val){
            p.next = l2;
            l2 = l2.next;
        }else{
            p.next = l1;
            l1 = l1.next;
        }
        p = p.next;
    }
    return x.next;
}
//Min:156ms