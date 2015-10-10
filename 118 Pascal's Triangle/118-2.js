var generate = function(numRows){
    //宣告陣列長
    var x = new Array();
    for( var i = 0; i < numRows; i++){
        //宣告各陣列寬
        var x[i] = new Array();
        x[i][i]=1;
        x[i][0]=1;
        for( var j = 0; j <= i; j++ ){
            //取上層相加
            x[i][j] = x[i-1][j] + x[i-1][j-1];
        }
    }
    return x;
}
//Min:116ms
