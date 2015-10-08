var maxDepth = function(root){
    var x, y;
    if(root){
        x = maxDepth(root.left);
        y = maxDepth(root.right);
    }else{
        return 0;
    }
    return (x>=y) ? (x+1) : (y+1);
}
//Min:128ms