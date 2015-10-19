int minDepth(struct TreeNode* root){
    int x, y;
    if(root){
        x = minDepth(root->left);
        y = minDepth(root->right);
        if(x==0 || y==0)
            return (x==0) ? y+1 : x+1;
        return (x <= y) ? x+1 : y+1;
    }else{
        return 0;
    }
}
//Min:4ms