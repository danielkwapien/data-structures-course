import unittest
from phase1 import SList2


class Test(unittest.TestCase):

    # setUp is a method which is ran before a test method is executed.
    # This is useful if you need some data (for example) to be present before running a test.
    def setUp(self):
        self.list = SList2()

    def test01(self):
        print('\nTEST delLargestSeq()')
        print('\nExample 1: Largest sequence of equal numbers')
        [self.list.addLast(i) for i in [3, 3, 3, 4, 5, 6, 6, 6, 7, 7, 7, 7, 2]]
        self.list.delLargestSeq()
        self.assertEqual('[3,3,3,4,5,6,6,6,2]', ('[' + str(self.list) + ']'))

    def test02(self):
        print('\nExample 2: Last largest sequence of equal numbers')
        [self.list.addLast(i) for i in [8, 8, 8, 8, 4, 5, 6, 6, 6, 7, 7, 7, 7, 2]]
        self.list.delLargestSeq()
        self.assertEqual('[8,8,8,8,4,5,6,6,6,2]', ('[' + str(self.list) + ']'))

    def test03(self):
        print('\nExample 3: No largest sequence')
        [self.list.addLast(i) for i in [6, 6, 8, 8, 4, 4, 12, 12]]
        self.list.delLargestSeq()
        self.assertEqual('[6,6,8,8,4,4]', ('[' + str(self.list) + ']'))

    def test04(self):
        print('\nExample 4: Valid sequence')
        [self.list.addLast(i) for i in [1, 2, 3, 4, 5]]
        self.list.delLargestSeq()
        self.assertEqual('[1,2,3,4]', ('[' + str(self.list) + ']'))

    def test05(self):
        print('\nExample 5: One element')
        [self.list.addLast(i) for i in [10]]
        self.list.delLargestSeq()
        self.assertEqual('[]', ('[' + str(self.list) + ']'))

    def test06(self):
        print('\nExample 6: Empty list')
        [self.list.addLast(i) for i in [None]]
        self.list.delLargestSeq()
        self.assertEqual('[]', ('[' + str(self.list) + ']'))

    def test07(self):
        print('\nTEST fix_loop()')
        print('\nExample 1: No loop')
        [self.list.addLast(i) for i in [1, 2, 3]]
        output = self.list.fix_loop()
        self.assertEqual('[1,2,3]', ('[' + str(self.list) + ']'))
        self.assertEqual(False, output)

    def test08(self):
        print('\nExample 2: Loop from last to first')
        [self.list.addLast(i) for i in [1, 2, 3]]
        self.list.create_loop(0)
        output = self.list.fix_loop()
        self.assertEqual('[1,2,3]', ('[' + str(self.list) + ']'))
        self.assertEqual(True, output)

    def test09(self):
        print('\nExample 3: Loop from last to second')
        [self.list.addLast(i) for i in [1, 2, 3]]
        self.list.create_loop(1)
        output = self.list.fix_loop()
        self.assertEqual('[1,2,3]', ('[' + str(self.list) + ']'))
        self.assertEqual(True, output)

    def test10(self):
        print('\nTEST leftrightShift()')
        print('\nExample 1: left = True, n = 2')
        [self.list.addLast(i) for i in [1, 2, 3, 4, 5, 6, 7]]
        self.list.leftrightShift(left=True, n=2)
        self.assertEqual('[3,4,5,6,7,1,2]', ('[' + str(self.list) + ']'))

    def test11(self):
        print('\nExample 2: left = True, n = 1')
        [self.list.addLast(i) for i in [1, 2, 3, 4, 5, 6, 7]]
        self.list.leftrightShift(left=True, n=1)
        self.assertEqual('[2,3,4,5,6,7,1]', ('[' + str(self.list) + ']'))

    def test12(self):
        print('\nExample 3: left = True, n = 4')
        [self.list.addLast(i) for i in [1, 2, 3, 4, 5, 6, 7]]
        self.list.leftrightShift(left=True, n=4)
        self.assertEqual('[5,6,7,1,2,3,4]', ('[' + str(self.list) + ']'))

    def test13(self):
        print('\nExample 4: left = False, n = 2')
        [self.list.addLast(i) for i in [1, 2, 3, 4, 5, 6, 7]]
        self.list.leftrightShift(left=False, n=2)
        self.assertEqual('[6,7,1,2,3,4,5]', ('[' + str(self.list) + ']'))

    def test14(self):
        print('\nExample 5: left = False, n = 1')
        [self.list.addLast(i) for i in [1, 2, 3, 4, 5, 6, 7]]
        self.list.leftrightShift(left=False, n=1)
        self.assertEqual('[7,1,2,3,4,5,6]', ('[' + str(self.list) + ']'))

    def test15(self):
        print('\nExample 6: left = False, n = 7')
        [self.list.addLast(i) for i in [1, 2, 3, 4, 5, 6, 7]]
        self.list.leftrightShift(left=False, n=7)
        self.assertEqual('[1,2,3,4,5,6,7]', ('[' + str(self.list) + ']'))

    def test16(self):
        print('\nExample 7: left = True, n = 10')
        [self.list.addLast(i) for i in [1, 2, 3, 4, 5, 6, 7]]
        self.list.leftrightShift(left=False, n=10)
        self.assertEqual('[1,2,3,4,5,6,7]', ('[' + str(self.list) + ']'))

    def test17(self):
        print('\nExample 8: Empty list')
        self.list.leftrightShift(left=False, n=2)
        self.assertEqual('[]', ('[' + str(self.list) + ']'))

 


if __name__ == "__main__":
    unittest.main()
