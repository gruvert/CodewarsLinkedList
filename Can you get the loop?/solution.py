def loop_size(node):
    slow = node
    fast = node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    if slow != fast:
        return 0

    # Знайдемо довжину циклу
    length = 1
    slow = slow.next
    while slow != fast:
        slow = slow.next
        length += 1

    return length
