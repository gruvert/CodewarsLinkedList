from preloaded import Node

def swap_pairs(head):
    new = Node(next=head)
    current = new
    while current.next and current.next.next:
        first = current.next
        second = current.next.next
        current.next = second
        first.next = second.next
        second.next = first
        current = first
    return new.next
