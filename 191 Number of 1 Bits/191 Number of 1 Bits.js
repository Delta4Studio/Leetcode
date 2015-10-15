var hammingWeight = function(n){
    var x = 0;
    while(n !== 0){
        x += n % 2;
        n = n>>>1;
    }
    return x;
}
//Min:144ms