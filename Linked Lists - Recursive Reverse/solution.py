class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    def recursive(cur, prev):
        if not cur:
            return prev
        next = cur.next
        cur.next = prev
        return recursive(next, cur)
    return recursive(head, None)
