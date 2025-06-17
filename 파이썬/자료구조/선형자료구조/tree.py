class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.childs = []
        
class Tree:
    def __init__(self, node=None):
        self.root = node
        
    def setRoot(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            return None
    
    def root(self):
        if self.root is None:
            return None
        else:
            return self.root
    
    def parent(self, node):
        if node.parent is None:
            return None
        else:
            return node.parent
    
    def children(self, node):
        if node.childs:
            return node.childs
        else:
            return None
        
    def child(self, node, n):
        if node.childs & len(node.childs) >= n:
            return node.childs[n-1]
        else:
            return None
    
    def retrieve(self, node):
        return node.data
    
    def is_root(self, node):
        if node == self.root:
            return True
        else:
            return False
    
    def is_reaf(self, node):
        if not node.childs:
            return True
        else:
            return False
    
    def degree(self, node):
        return len(node.childs)
    
    def size(self, node=root):
        size_val = 1
        for i in node.childs:
            size_val += size(i)
        
    # def height(self):
        
    def attach(self, node, data):
        newNode = Node(data)
        newNode.parent = node
        node.childs.append(newNode)
        
    def attach(self, node, tree):
        if tree.root is None:
            return None
        else:
            tree.root.parent = node
            node.childs.append(tree.root)
    
    def detach(self, node):
        parent = node.parent
        parent.childs.remove(node)
        node.parent = None
        return Tree(node)