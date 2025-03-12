/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    let pos = 0;
    for (let i = 0; i < nums.length; i++) { //remember to initialise the variable with let; need to index array unlike python
        if (nums[i] !== val) {
            nums[pos++] = nums[i];
        }
    }
    return pos;
    };
