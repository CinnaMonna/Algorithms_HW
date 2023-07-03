import enum

class Color(enum.Enum):
    RED = True
    BLACK = False
 
class Node:
    def __init__(self, value):
        self.val = value
        self.color = Color.RED
        self.left = None
        self.right = None
 
class Red_black_tree:
    def __init__(self):
        self.root = None
 
    def add(self, value) -> None:
        print('add', value)
        self.root = self.__add(self.root, value)
        self.root.color = Color.BLACK
 
    def __add(self, root: Node, val) -> Node:
        if root is None:
            return Node(val)
 
        if val < root.val:
            root.left = self.__add(root.left, val)
        elif val > root.val:
            root.right = self.__add(root.right, val)
        else:
            root.val = val
 
        if self.is_red(root.right) and not self.is_red(root.left):
            root = self.left_swap(root)
        if self.is_red(root.left) and self.is_red(root.left.left):
            root = self.right_swap(root)
        if self.is_red(root.left) and self.is_red(root.right):
            self.color_swap(root)    

        return root
 
    @staticmethod
    def is_red(node: Node) -> bool:
        if node is None:
            return False
        return node.color == Color.RED
 
    @staticmethod
    def color_swap(node: Node) -> None:
        node.color = Color.RED
        node.left.color = Color.BLACK
        node.right.color = Color.BLACK
 
    def left_swap(self, node: Node) -> Node:
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
 
        new_root.color = node.color
        node.color = Color.RED
        print("Left swap")
        return new_root
 
    def right_swap(self, node: Node) -> Node:
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
 
        new_root.color = node.color
        node.color = Color.RED
        print("Right swap")
        return new_root
 
    def inorder(self) -> None:
        self.__inorder(self.root)
 
    def __inorder(self, root: Node) -> None:
        if root is None:
            return
        self.__inorder(root.left)
        print(root.val, end=" ")
        self.__inorder(root.right)
 
 
Red_black_tree = Red_black_tree()
Red_black_tree.add(10)
Red_black_tree.add(20)
Red_black_tree.add(30)
Red_black_tree.add(40)
Red_black_tree.add(50)
Red_black_tree.add(25)
Red_black_tree.inorder()

 


    
