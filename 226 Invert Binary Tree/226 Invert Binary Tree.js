var invertTree = function(root){
    if(root){
        var x = root.left;
        root.left = invertTree(root.right);
        root.right = invertTree(x);
        return root;
    }else{
        return null;
    }
};
//Min:112ms