/** note that function defined in a different way to JS:
function RemoveElement() rather than var removeEelemnt = function(nums,val) {
**/

function removeElement(nums: number[], val: number): number {
    let pos: number = 0; //note number not integer
    for (let i: number = 0; i < nums.length; i++) {
        if (nums[i] !== val) {
            nums[pos++] = nums[i];
        }
    }
    return pos;
    };
