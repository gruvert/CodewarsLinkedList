""" For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""
def sorted_insert(head, data):
    result = Node(data)
    if head is None or head.data >= data:
        result.next = head
        return result
    current = head
    while current.next and current.next.data < data:
        current = current.next
    result.next = current.next
    current.next = result
    return head
