/** typescript implementation of validparentheses.py **/

function isValid(s: string): boolean {
    const openBrackets: string[] = ['(','[','{']; //note the need to specifically declare the list contents type
    const closeBrackets: string[] = [')',']','}'];
    const parentheses: string[] = [] // Similar to python -> parentheses: List[str] = []

    for (let i of s) {
        if (openBrackets.includes(i)) {
            parentheses.push(i); // use list.push() rather than list.append()
        } else if (closeBrackets.includes(i)) {
            if (!parentheses.length) {
                return false;
            }
            if (closeBrackets.indexOf(i) !== openBrackets.indexOf(parentheses.pop())) { //note the capitilisastion of "Of" in "indexOf"
                return false;
            }
        }
    }

    return !parentheses.length;
};
