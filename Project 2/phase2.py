"""
@author: EDA Team
"""

# Classes provided by EDA Team
from bintree import BinaryNode
from bst import BinarySearchTree


# Exercise #1
class BST2(BinarySearchTree):
    def find_dist_k(self, n: int, k: int) -> list:
        target_node = self.search(n)
        if target_node is None:
            return []
        return self._find_dist_k(target_node, k, self._root)

    def _find_dist_k(self, node, k, temp):1º
        if not temp:
            return []
        distance = self.distance(temp, node)
        nodes = []
        if distance == k:
            nodes = [temp.elem]
        if temp.left:
            nodes += self._find_dist_k(node, k, temp.left)
        if temp.right:
            nodes += self._find_dist_k(node, k, temp.right)
        return nodes

    def lca(self, temp, a, b):
        if not temp:
            return
        if temp.elem < a.elem and temp.elem < b.elem:
            return self.lca(temp.right, a, b)
        if temp.elem > a.elem and temp.elem > b.elem:
            return self.lca(temp.left, a, b)
        else:
            return temp

    def _distance(self, temp, a):
        if not temp:
            return 0
        distance = 1
        if temp.elem == a.elem:
            return 0
        if temp.elem > a.elem:
            distance += self._distance(temp.left, a)
        else:
            distance += self._distance(temp.right, a)
        return distance

    def distance(self, a, b):
        lca = self.lca(self._root, a, b)
        distance_a = self._distance(lca, a)
        distance_b = self._distance(lca, b)
        return distance_b + distance_a


# Exercise #2
def create_tree(input_tree1: BinarySearchTree, input_tree2: BinarySearchTree, opc: str) -> BinarySearchTree:
    # Here your code
    tree = None
    if opc == "merge":
        if input_tree1.size() > input_tree2.size():
            tree = merge(input_tree1, input_tree2)
        else:
            tree = merge(input_tree2, input_tree1)
    elif opc == "intersection":
        if input_tree1.size() > input_tree2.size():
            tree = intersect(input_tree1, input_tree2)
        else:
            tree = intersect(input_tree1, input_tree2)

    elif opc == "difference":
        tree = difference(input_tree1, input_tree2)
    else:
        print("Please select a valid option")
    return tree


def merge(tree1: BinarySearchTree, tree2: BinarySearchTree) -> BinarySearchTree:
    res = tree1
    _merge(res, tree2._root)
    return res


def _merge(tree: BinarySearchTree, node: BinaryNode):
    if node is None:
        return
    else:
        _merge(tree, node.left)
        tree.insert(node.elem)
        _merge(tree, node.right)


def intersect(tree1: BinarySearchTree, tree2: BinarySearchTree) -> BinarySearchTree:
    res = BinarySearchTree()
    _intersect(res, tree1._root, tree2)
    return res


def _intersect(res: BinarySearchTree, node1, tree2: BinarySearchTree):
    if node1 is None:
        return
    else:
        if mySearch(node1.elem, tree2._root):
            res.insert(node1.elem)
        _intersect(res, node1.left, tree2)
        _intersect(res, node1.right, tree2)


def difference(tree1: BinarySearchTree, tree2: BinarySearchTree) -> BinarySearchTree:
    res = BinarySearchTree()
    _difference(res, tree1._root, tree2)
    return res


def _difference(res: BinarySearchTree, node1: BinaryNode, tree2: BinarySearchTree):
    if node1 is None:
        return
    else:
        if not mySearch(node1.elem, tree2._root):
            res.insert(node1.elem)
        _difference(res, node1.left, tree2)
        _difference(res, node1.right, tree2)


def mySearch(elem, node: BinaryNode):
    if node is None:
        return False
    else:
        if elem == node.elem:
            return True
        else:
            if elem < node.elem:
                res = mySearch(elem, node.left)
            else:
                res = mySearch(elem, node.right)
            return res


# Some usage examples
if __name__ == '__main__':
    # input_list_01 = [5, 1, 7, 9, 23]
    # input_list_02 = [1, 9, 11]
    input_list_01 = [5, 12, 2, 1, 3, 9]
    input_list_02 = [9, 3, 21]
    input_list_03 = [9, 3, 21, 12, 24, 4, 2]

    # Build and draw first tree
    tree1 = BinarySearchTree()
    for x in input_list_01:
        tree1.insert(x)
    print("Tree 1:")
    tree1.draw()

    # Build and draw second tree
    tree2 = BinarySearchTree()
    for x in input_list_02:
        tree2.insert(x)
    print("Tree 2:")
    tree2.draw()

    function_names = ["merge", "intersection", "difference"]

    for op_name in function_names:
        res = create_tree(tree1, tree2, op_name)
        print(f"-- Result for {op_name} method applied to tree 1 and tree 2. #{res.size()} nodes")
        res.draw()
        if op_name == "merge":
            tree1 = BinarySearchTree()
            for x in input_list_01:
                tree1.insert(x)
            tree2 = BinarySearchTree()
            for x in input_list_02:
                tree2.insert(x)
