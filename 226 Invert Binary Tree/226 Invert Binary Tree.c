struct TreeNode* invertTree(struct TreeNode* root){
    if(root){
        struct TreeNode* p = root->lrft;
        root->left = invertTree(root->right);
        root->right = invertTree(p);
        return root;
    }
}
//Min:0ms