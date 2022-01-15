
import json

class Node():
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return json.dumps(BST.create_tree_structure(self))
        # return f"Node(val={self.val})"

class BST():
    def __init__(self):
        self.root = None

    def _get_max_or_min_val(self, removal_node: Node, right_or_left: str):
        cn = removal_node.right if right_or_left == 'right' else removal_node.left
        if right_or_left == "right":
            while cn.left.left:
                cn = cn.left
                continue
            removal_node.val = cn.left.val
            cn.left = None
        else:
            while cn.right.right:
                cn = cn.right
                continue
            removal_node.val = cn.right.val
            cn.right = None

    def remove(self, val):
        if not self.root:
            return False
        cn = self.root
        while cn:
            if cn and cn.val == val:
                if cn.left:
                    self._get_max_or_min_val(cn.left, 'max')
                elif cn.right:
                    self._get_max_or_min_val(cn.right, 'min')
                else:
                    self.root = None
                
            if cn and val < cn.val:
                if cn.left and cn.left.val == val:
                    if cn.left.left:
                        self._get_max_or_min_val(cn.left, 'left')
                    elif cn.left.right:
                        self._get_max_or_min_val(cn.left, 'right')
                    else:
                        cn.left = None
                else:
                    cn = cn.left
            if cn and val > cn.val:
                if cn.right and cn.right.val == val:
                    if cn.right.left:
                        self._get_max_or_min_val(cn.right, 'left')
                    elif cn.right.right:
                        self._get_max_or_min_val(cn.right, 'right')
                    else:
                        cn.left = None
                else:
                    cn = cn.right

    def insert(self, val: int):
        node = Node(val)
        if not self.root:
            self.root = node
            return
        def _recursive_insert(current_node):
            if node.val <= current_node.val:
                if not current_node.left:
                    current_node.left = node
                    return
                _recursive_insert(current_node.left)
            else:
                if not current_node.right:
                    current_node.right = node
                    return
                _recursive_insert(current_node.right)

        _recursive_insert(self.root)

    def lookup(self, val):
        if not self.root:
            return False
        cn = self.root
        while cn:
            if val == cn.val:
                return cn
            elif val < cn.val:
                cn = cn.left
            else:
                cn = cn.right
        return False

    @staticmethod
    def print_tree_bft(node: Node = None):
        l = []
        l.append(node)

        while l:
            print(l[0].val)
            if l[0].left:
                l.append(l[0].left)
            if l[0].right: 
                l.append(l[0].right)
            l = l[1:]
    
    @staticmethod
    def create_tree_structure(node: Node):
        tree = {'value' : node.val}
        tree['left'] = node.left if not node.left else BST.create_tree_structure(node.left)
        tree['right'] = node.right if not node.right else BST.create_tree_structure(node.right)
        return tree

bst = BST()
bst.insert(5)
bst.insert(7)
bst.insert(4)
bst.insert(1)
bst.insert(6)
bst.insert(50)
bst.insert(18)
bst.insert(20)
bst.insert(16)
bst.insert(13)
bst.insert(19)
bst.insert(22)
bst.insert(70)
bst.insert(51)
bst.insert(75)

# print(bst.print_tree_bft(bst.root))
print(json.dumps(bst.create_tree_structure(bst.root)))

# print(bst.lookup(4))
# print(bst.lookup(40))

bst.remove(50)
print('\n\n\n')
print(json.dumps(bst.create_tree_structure(bst.root)))