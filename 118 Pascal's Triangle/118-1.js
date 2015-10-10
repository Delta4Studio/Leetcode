var generate = function(numRows){
    //宣告陣列長 
    var x = new Array(); 
    for( var i = 0; i < numRows; i++){ 
        //宣告各陣列寬 
        var x[i] = new Array();
        for( var j = 0; j <= i; j++ ){ 
            //判斷是否為頭尾，否則取上層相加 
            ( j === 0 || j === i ) ? x[i][j] = 1 : x[i][j] = x[i-1][j] + x[i-1][j-1]; 
        } 
    } 
    return x; 
}
//Min:120ms 
