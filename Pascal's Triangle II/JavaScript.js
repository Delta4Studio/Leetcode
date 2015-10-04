var getRow = function(rowIndex){ 
    var x = [1], t = 1; 
    rowIndex++; 
    for(var i = 1; i < rowIndex; i++){
        t = t * (rowIndex * i) / i;
        x.push(t); 
    } 
    return x; 
}
//Min:112ms