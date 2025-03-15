/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    const words = s.trim().split(/\s+/);
    return words.length > 0 ? words[words.length - 1].length: 0;
};

/**
s.trim() removes white space from the beginning and end
s.split(/\s+/) splits the sentence into tokens based on one or more spaces between words
words.length > 0 returns:
-- the length of words[words.length -1].length if words has a length > 0 
-- returns 0 if length = 0
words.length returns the number of items in the array
words[words.length -1] returns the last item in the array
words[words.length - 1].length returns the length of the last item in the array

**/
