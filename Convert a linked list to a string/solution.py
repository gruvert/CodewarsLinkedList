def stringify(node):
    string = ''
    if node:
        while True:
            if node:
                string += str(node.data) + ' -> '
                node = node.next
            else: 
                string += 'None'
                return string
    return 'None'
