var maxProfit = function(prices){
    if(prices.length <= 1)
        return 0;
    var minValue = maxValue = prices[0], value = max = 0;
    for(var i=1; i < prices.length; i++){
        if(prices[i] > maxValue){
            maxValue = prices[i];
        }else if(prices[i] < minValue){
            value = maxValue - minValue;
            max = (max > value) ? max : value;
            minValue = prices[i];
        }
    }
    return (value > max) ? value : max;
};
//Min:132ms