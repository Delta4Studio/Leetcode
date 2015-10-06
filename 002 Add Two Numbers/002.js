/**
 * function ListNodefunction(val){
 *     this.val = val;
 *     this.next = null;
 * }
**/
var addTwoNumbers = function(l1, l2){
    var x = new ListNode(0);
    //pointer
    var p = x, p1 = l1, p2 = l2;
    //temp
    var carry = 0, v1, v2;
    
    while(p1||p2){
        if(p1){
            v1 = p1.val;
            p1 = p1.next;
        }else{
            v1 = 0;
        }
        if(p2){
            v2 = p2.val;
            p2 = p2.next;
        }else{
            v2 = 0;
        }
        var t = carry + v1 + v2;
        if(t > 9){
            carry = 1;
            t = t % 10;
        }else{
            carry = 0;
        }
        p.next = new ListNode(t);
        p = p.next;
    }
    if(carry!==0)
        p.next = new ListNode(1);
    return x.next;
}
//Min:236ms