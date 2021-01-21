class AVLNode:
    def __init__(self, data, left=None, right=None, parent=None):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.bf = 0  # balance factor: the height of left - the height of right


class AVLTree:
    def __init__(self):
        self.root = None

    def _printerHelper(self, currPtr, indent, last):
        """ Print the tree structure on the screen"""
        if currPtr:
            pass

    def prettyPrint(self):
        self._printerHelper(self.root, "", True)

    def insert(self, key):
        node = AVLNode(key)
        parent = None
        cur = self.root

        # Insert the new node
        while cur:
            parent = cur
            cur = cur.right if cur.data < key else cur.left

        node.parent = parent
        if not parent: # parent is None
            self.root = node
        elif key < parent.data:
            parent.left = node
        else:
            parent.right = node

        # Update balance factor and rebalance
        self._updateBalance(node)

    def _updateBalance(self, node):
        if node.bf < -1 or node.bf > 1:  # Balance factor 2 或者 -2的时候就对该结点进行再平衡
            self._rebalance(node)
            return

        if node.parent:
            if node is node.parent.left:
                node.parent.bf += 1
            else:
                node.parent.bf -= 1

            if node.parent.bf != 0:  # 父结点的balance factor 不为0的时候需要递归调用更新祖先结点
                self._updateBalance(node.parent)

    def _rebalance(self, node):
        if node.bf > 0:  # LL or LR case， node bf 为 2
            if node.right.bf < 0:
                self.leftRotate(node.right)
                self.rightRotate(node)
            else:
                self.rightRotate(node)

        if node.bf < 0:  # RR or RL case， node bf 为 -2
            if node.right.bf > 0:
                self.rightRotate(node.right)
                self.leftRotate(node)
            else:
                self.leftRotate(node)

    def leftRotate(self, node):
        new_top = node.right

        node.right = new_top.left
        if new_top.left:
            new_top.left.parent = node

        new_top.parent = node.parent
        if not node.parent:
            self.root = new_top
        else:
            if node.parent.left is node:
                node.parent.left = new_top
            else:
                node.parent.right = new_top

        new_top.left = node
        node.parent = new_top

        # Update the balance factor of new_top and node
        node.bf = node.bf + 1 - min(new_top.bf, 0)
        new_top.bf = new_top.bf + 1 - max(node.bf, 0)

    def rightRotate(self, node):
        new_top = node.right
        node.left = new_top.right
        if new_top.right:
            new_top.right.parent = node

        new_top.parent = node.parent
        if not node.parent: # node.parent is None, node is root node
            self.root = new_top
        else:
            if node.parent.left is node:
                node.parent.left = new_top
            else:
                node.parent.right = new_top

        new_top.right = node
        node.parent = new_top

        # Update the balance factor of new_top and node
        node.bf = node.bf - 1 - max(new_top.bf, 0)
        new_top.bf = new_top.bf - 1 + min(node.bf, 0)

    def preorder(self, root):
        if root:
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)

if __name__ == '__main__':
    tree = AVLTree()
    # node = AVLNode(1)
    for i in range(6):
        tree.insert(i)

    # print(tree.root.data)
    tree.preorder(tree.root)












