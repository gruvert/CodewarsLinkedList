def linked_list_from_string(s):
    if s.lower() == "none":
        return None
    
    values = s.split(" -> ")
    head = Node(int(values[0]))
    current = head
    
    for val in values[1:]:
        if val.lower() == "none":
            break
        current.next = Node(int(val))
        current = current.next
        
    return head
