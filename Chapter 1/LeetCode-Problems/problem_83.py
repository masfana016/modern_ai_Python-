# 83. Remove Duplicates from Sorted List

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # Edge case: if the list is empty, return None
        if not head:
            return None

        # Initialize the current node as the head
        current = head

        # Traverse the list
        while current and current.next:
            # If the current node's value is equal to the next node's value
            if current.val == current.next.val:
                # Skip the next node
                current.next = current.next.next
            else:
                # Otherwise, move to the next node
                current = current.next

        return head

    
# Step 1: Helper function to convert list to linked list
def list_to_linkedlist(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Step 2: Helper function to convert linked list back to list
def linkedlist_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Step 3: Create linked list input
input_list = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 5, 5 ,5 ,6 ,6 , 6,6 ,6, 6, 6]
head = list_to_linkedlist(input_list)

# Step 4: Call the function
solution = Solution()
new_head = solution.deleteDuplicates(head)

# Step 5: Print result as list
print(linkedlist_to_list(new_head))  # Output: [1, 2]

        