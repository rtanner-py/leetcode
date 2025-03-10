/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode | null {
    let dummy = new ListNode();
    let current: ListNode = dummy; // note the reference to the type : ListNode

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

    /**
    Note the change underneath from JS. 
    Previously used current.next = list1 ? list1 : list2; 
    Now need to explicitly say list1 !== null
    **/
  
    current.next = list1 !== null ? list1 : list2;
    return dummy.next;
};
