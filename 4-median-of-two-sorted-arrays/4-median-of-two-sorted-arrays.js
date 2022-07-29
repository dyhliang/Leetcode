/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    let merged_arr = nums1.concat(nums2);
    merged_arr.sort();
    
    merged_arr.sort(function(a, b) {
        return a - b;
    });
    
    if(merged_arr.length % 2 == 0){
        let left = merged_arr[parseInt(merged_arr.length / 2 - 1)]; 
        let right = merged_arr[parseInt(merged_arr.length / 2)];
        return (left + right) / 2;
    }
    else{
        return merged_arr[parseInt(merged_arr.length / 2)];
    };
};