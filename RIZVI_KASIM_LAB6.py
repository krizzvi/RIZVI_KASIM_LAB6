class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def get_cycle_length(node):
    # Step 1: Detect if there is a cycle
    slow, fast = node, node

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:  # Cycle detected
            # Step 2: Calculate the cycle length
            return calculate_cycle_length(slow)

    return 0  # No cycle


def calculate_cycle_length(meeting_point):
    current = meeting_point
    length = 0

    while True:
        current = current.next
        length += 1
        if current == meeting_point:
            break

    return length


# Example Usage:
# Creating a list: 5 -> 2 -> 3 -> 4 -> 1 -> (cycle back to 2)
head = ListNode(5)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1 = ListNode(1)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node1
node1.next = node2  # Cycle

print(get_cycle_length(head))  # Should return 4 (cycle length)