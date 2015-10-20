struct ListNode* reverseList(struct ListNode* head){
    struct ListNode *cp = head, *np = NULL, *pp;
    while(cp!=NULL){
        pp = cp->next;
        cp->next = np;
        np = cp;
        cp = pp;
    }
    return np;
}
//Min:0ms