class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
    
def move_node(source, dest):
    if not source:
        raise Exception
    if not dest:
        dest = Node(source.data)
    else:
        dest = push(dest, source.data)
    if source.next:
        source = source.next
    else:
        source = None
    return Context(source, dest)
