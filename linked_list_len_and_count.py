class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def length(node):
    return 1 + length(node.next) if node else 0

def count(node, data):
    if node is None:
        return 0
    return 1 + count(node.next, data) if node.data == data else count(node.next, data)
