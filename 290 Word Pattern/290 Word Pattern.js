/**
 * @param {string} pattern
 * @param {string} str
 * @return {boolean}
 */
var wordPattern = function(pattern, str) {
    var ptmp = pattern.split("");
    var stmp = str.split(" ");
    var json = {};
    var sch = [];
    if(stmp.length != ptmp.length)
        return false;
    for(var i = 0; i < ptmp.length; i++){
        if(json[ptmp[i]] == undefined){
            for(var j=0;j<sch.length;j++){
                if(json[sch[j]] == stmp[i])
                    return false;
            }
            sch.push(ptmp[i]);
        }
        json[ptmp[i]] = stmp[i];
    }
    for(i = 0; i < ptmp.length; i++){
        if (json[ptmp[i]] != stmp[i])
            return false;
    }
    return true;
};
//Min:112ms