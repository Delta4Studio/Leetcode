var isSameTree(p, q){
    var x, y;
    if(p||q){
        if((p != null) && (q != null)){
            if(p.val == q.val){
                x = isSameTree(p.left, q.left);
                y = isSameTree(p.right, q.right);
            }else{
                return false;
            }
        }else{
            return false;
        }
    }else{
        return true;
    }
    if(x&&y){
        return true;
    }else{
        return false;
    }
}
//Min:108ms