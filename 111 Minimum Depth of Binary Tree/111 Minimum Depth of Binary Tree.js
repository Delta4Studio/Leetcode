var minDepth = function(root){
    var x, y;
    if(root){
        x = minDepth(root.left);
        y = minDepth(root.right);
        if(x==0 || y==0){
            if(x==0)
                return y+1;
            return x+1;
        }
        return (x<=y) ? (x+1) : (y+1);
    }else{
        return 0;
    }
}
//Min:132ms