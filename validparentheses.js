/** Javascript implementation of the validparentheses.py solution **/

/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const openBrackets = ['(','[','{'];
    const closeBrackets = [')',']','}'];
    const parentheses = [];

    for (let i of s) {
        if (openBrackets.includes(i)) {
            parentheses.push(i);
        } else if (closeBrackets.includes(i)) {
            if (!parentheses.length) {
                return false;
            }
            if (closeBrackets.indexOf(i) !== openBrackets.indexOf(parentheses.pop())) {
                return false;
            }
        }
    }
    return !parentheses.length;
};
