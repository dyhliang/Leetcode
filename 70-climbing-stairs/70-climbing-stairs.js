/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    if (n <= 3){
        return n;
    } else {
        let prev_prev = 1;
        let prev = 2;
        let total = 3;
        let curr = 3;
        
        while (curr < n){
            prevprev = prev;
            prev = total;
            total = total + prevprev;
            curr++;
        }
        
        return total;
    }
};