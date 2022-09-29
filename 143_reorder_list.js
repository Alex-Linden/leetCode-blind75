/**You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 */

var reorderList = function (head) {
  let secondHalf = getMid(head);
  secondHalf = reverseLL(secondHalf);
  reorder(head, secondHalf);

};


function getMid(head) {
  let fast = head;
  let slow = head;
  while (fast && fast.next) {
    slow = slow.next;
    fast = fast.next.next;
  }
  return slow;
}

function reverseLL(head) {
  let [prev, curr, next] = [null, head, null];

  while (curr) {/* Time O(N) */
    next = curr.next;
    curr.next = prev;

    prev = curr;
    curr = next;
  }
  return prev;
}

function reorder(list1, list2) {
  let [first, next, second] = [list1, null, list2];

  while (second.next) {
    next = first.next;
    first.next = second;
    first = next;

    next = second.next;
    second.next = first;
    second = next;
  }
}