var maxProfit = function(prices){
    var tmp=0, sum=0;
    for(var i=0; i<prices.length; i++){
        if ( i!=0 && tmp < prices[i])
            sum += (prices[i] - tmp);
        tmp = prices[i];
    }
    return sum;
};
//Min:132ms