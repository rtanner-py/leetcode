/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(list1, list2) {
    /**
    - Can create variables in two ways main ways. Use let for variables that change; const for fixed variables;
    - Use new when creating instances of a class (see below) so that it uses a constructor [note the
    reference to 'this' in the function] otherwise it will throw an error [It tries to treat it as a normal 
    functional call, but will error because it uses this]
    - Don't use var because it has function scoping issues.
    **/
    let dummy = new ListNode();
    let current = dummy;

    while (list1 && list2) {
        if (list1.val < list2.val) {
            current.next = list1;
            list1 = list1.next;
        } else {
            current.next = list2;
            list2 = list2.next;
        }
        current = current.next;
    }

    current.next = list1 ? list1 : list2;

    return dummy.next;
};
