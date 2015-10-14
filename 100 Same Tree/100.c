bool isSameTree(struct TreeNode* p, struct TreeNode* q){
    bool x, y;
    if((p!=NULL)&&(q!=NULL)){
        if(p->val == q->val){
            x = isSameTree(p->left, q->left);
            y = isSameTree(p->right, q->right);
        }else{
            return false;
        }
    }else if((q==NULL)&&(p==NULL)){
        return true;
    }else{
        return false;
    }
    if(x&&y){
        return true;
    }else{
        return false;
    }
}
//Min:0ms