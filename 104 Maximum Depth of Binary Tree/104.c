int maxDepth(struct TreeNode* root){
    int x, y;
    if(root){
        x = maxDepth(root->left);
        y = maxDepth(root->right);
    }else{
        return 0;
    }
    return (x >= y) ? (x+1) : (y+1);
}
//Min:4ms