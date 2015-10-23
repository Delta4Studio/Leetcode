int maxProfit(int* prices, int pricesSize){
    int tmp=0, sum = 0,i;
    for(i=0; i<pricesSize; i++){
        if(i!=0 && tmp < *(prices+i))
            sum += (*(prices+i) - tmp);
        tmp = *(prices+i);
    }
    return sum;
}
//Min:4ms