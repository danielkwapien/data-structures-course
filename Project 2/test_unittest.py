# -*- coding: utf-8 -*-

from bst import BinarySearchTree
import unittest
from phase2 import BST2
from phase2 import create_tree, merge, _merge, intersect, _intersect, difference, _difference, mySearch




class Test(unittest.TestCase):
    def setUp(self):
        self.tree = BST2()
        self.function_names = ["merge", "intersection", "difference"]

    def test_test01(self):
        print('\nfind_dist_k(n, k)')
        print('\nExample 1: n = 30 and k = 0')
        [self.tree.insert(i) for i in [16, 8, 24, 4, 12, 20, 28, 2, 6, 10, 14, 18, 22, 26, 30, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]]
        self.assertEqual('[30]', (str(self.tree.find_dist_k(30, 0))))

    def test_test02(self):
        print('\nExample 2: n = 30 and k = 2')
        [self.tree.insert(i) for i in [16, 8, 24, 4, 12, 20, 28, 2, 6, 10, 14, 18, 22, 26, 30, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]]
        self.assertEqual('[24, 26]', (str(self.tree.find_dist_k(30, 2))))

    def test_test03(self):
        print('\nExample 3: n = 23 and k = 4')
        [self.tree.insert(i) for i in [16, 8, 24, 4, 12, 20, 28, 2, 6, 10, 14, 18, 22, 26, 30, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]]
        self.assertEqual('[16, 17, 19, 28]', (str(self.tree.find_dist_k(23, 4))))

    def test_test04(self):
        print('\nExample 4: n = 27 and k = 7')
        [self.tree.insert(i) for i in [16, 8, 24, 4, 12, 20, 28, 2, 6, 10, 14, 18, 22, 26, 30, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]]
        self.assertEqual('[2, 6, 10, 14]', (str(self.tree.find_dist_k(27, 7))))

    def test_test05(self):
        print('\nExample 5: n = 1 and k = 8')
        [self.tree.insert(i) for i in [16, 8, 24, 4, 12, 20, 28, 2, 6, 10, 14, 18, 22, 26, 30, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]]
        self.assertEqual('[17, 19, 21, 23, 25, 27, 29]', (str(self.tree.find_dist_k(1, 8))))

    def test_test06(self):
        print('\n---------------------------')
        print('\ncreate_tree(tree1, tree2)')
        print('\nExample 1: tree1=[5, 12, 2, 1, 3, 9], treeB=[9, 3, 21], merge method')
        treeA = BinarySearchTree()
        for x in [5, 12, 2, 1, 3, 9]:
            treeA.insert(x)
        treeB = BinarySearchTree()
        for x in [9, 3, 21]:
            treeB.insert(x)

        expectedRes = BinarySearchTree()
        for x in [5, 2, 12, 21, 9, 3, 1]:
            expectedRes.insert(x)
        res = create_tree(treeA, treeB, "merge")
        self.assertEqual(str(expectedRes.inorder_list()), str(res.inorder_list()))

    def test_test07(self):
        print('\nExample 2: tree1=[5, 12, 2, 1, 3, 9], treeB=[9, 3, 21], intersection method')
        treeA = BinarySearchTree()
        for x in [5, 12, 2, 1, 3, 9]:
            treeA.insert(x)
        treeB = BinarySearchTree()
        for x in [9, 3, 21]:
            treeB.insert(x)
        expectedRes = BinarySearchTree()
        for x in [3, 9]:
            expectedRes.insert(x)
        res = create_tree(treeA, treeB, "intersection")
        self.assertEqual(str(expectedRes.inorder_list()), str(res.inorder_list()))

    def test_test08(self):
        print('\nExample 2: tree1=[5, 12, 2, 1, 3, 9], treeB=[9, 3, 21], difference method')
        treeA = BinarySearchTree()
        for x in [5, 12, 2, 1, 3, 9]:
            treeA.insert(x)
        treeB = BinarySearchTree()
        for x in [9, 3, 21]:
            treeB.insert(x)
        expectedRes = BinarySearchTree()
        for x in [5, 12, 2, 1]:
            expectedRes.insert(x)
        res = create_tree(treeA, treeB, "difference")
        self.assertEqual(str(expectedRes.inorder_list()), str(res.inorder_list()))


# Some usage examples
if __name__ == '__main__':
    unittest.main()
