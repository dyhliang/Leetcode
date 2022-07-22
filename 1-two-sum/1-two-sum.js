/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    prev = {}
    
    for (let i = 0; i < nums.length; i++){
        let diff = target - nums[i];
        
        if (diff in prev){
            return [prev[diff], i];
        }
        
        prev[nums[i]] = i;
        
    }
};