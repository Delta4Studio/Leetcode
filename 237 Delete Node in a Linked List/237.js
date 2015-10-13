var deleteNode = function(node){
    node.val = node.next.val;
    node.next = node.next.next;
}
//Min:132ms