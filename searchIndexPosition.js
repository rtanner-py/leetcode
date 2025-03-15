/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    if (nums.includes(target)) { //note that this is the same as (if num in list) in python
        return nums.indexOf(target);
    } else {
        nums.push(target); //adds target to the end of nums
        nums.sort(); // can use nums.sort((a,b) => a-b) to enforce numerical sorting, but is not required here.
        return nums.indexOf(target);
    }
};
