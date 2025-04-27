class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
    
    def set_next_node(self, next_node ):
        self.next_node = next_node
    
    def get_next_node(self):
        return self.next_node
        
    def get_value(self):
        return self.value
    

obj = Node(1)
print(obj.get_value())
print(obj.get_next_node())

obj.set_next_node(Node(2))
print(obj.get_next_node().get_value())
print(obj.get_next_node().get_next_node())
print(obj.get_next_node().get_next_node() is None)

