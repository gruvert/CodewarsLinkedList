class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if not head:
        raise Exception
    cur = head.next.next
    first = Node(head.data)
    second = Node(head.next.data)
    first_c = first
    second_c = second
    while cur:
        first_c.next = Node(cur.data)
        first_c = first_c.next
        if cur.next:
            second_c.next = Node(cur.next.data)
            second_c = second_c.next
            cur = cur.next.next
        else:
            break
    return Context(first, second)
