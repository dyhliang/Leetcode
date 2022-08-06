/**
 * @param {string} n
 * @return {number}
 */
var minPartitions = function(n) {
    let digits = [];
    
    for (let i = 0; i < n.length; i++){
        digits.push(n[i]);
    }
    
    return Math.max(...digits);
};