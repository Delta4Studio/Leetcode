int maxProfit(int* prices, int pricesSize){
    if (pricesSize <= 1){
        return 0;
    }
    int maxValue = *(prices), minValue = *(prices), max =0, value = 0, i;
    for(i=1; i < pricesSize; i++){
        if(*(prices+i) > maxValue){
            maxValue = *(prices+i);
        }else if(*(prices+i) < minValue){
            max = ((maxValue - minValue) > max) ? maxValue- minValue : max;
            minValue = maxValue = *(prices+i);
        } 
        return ((maxValue - minValue) > max) ? maxValue- minValue : max;
    }
}
//Min:4ms