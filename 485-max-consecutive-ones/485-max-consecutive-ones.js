/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxConsecutiveOnes = function(nums) {
    let consec = 0;
    let max_consec = consec;
    
    for (let i=0; i<nums.length; i++){
        if (nums[i] === 1){
            consec++;
            if(consec > max_consec){
                max_consec = consec;
            }
        } else {
            consec = 0;
        }
    }
    
    return max_consec;
};