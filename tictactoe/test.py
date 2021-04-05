from .model import SquareNav, LineNav
from unittest import TestCase

class TestNavClasses(TestCase):

    def testLineNav(self):
        ln = LineNav(3)
        self.assertEqual(ln.prev(0), None)
        self.assertEqual(ln.prev(1), 0)
        self.assertEqual(ln.prev(2), 1)
        self.assertEqual(ln.next(0), 1)
        self.assertEqual(ln.next(1), 2)
        self.assertEqual(ln.next(2), None)

    def testSquareNav(self):
        sn = SquareNav(3)

        self.assertEqual(sn.getCol(4), 1)
        self.assertEqual(sn.getCol(6), 0)
        self.assertEqual(sn.getRow(4), 1)
        self.assertEqual(sn.getRow(0), 0)
        self.assertEqual(sn.getRow(6), 2)

        self.assertEqual(sn.getNextInRow(0), 1)
        self.assertEqual(sn.getNextInRow(1), 2)
        self.assertEqual(sn.getNextInRow(2), None)
        self.assertEqual(sn.getNextInRow(3), 4)
        self.assertEqual(sn.getNextInRow(4), 5)
        self.assertEqual(sn.getNextInRow(5), None)
        self.assertEqual(sn.getNextInRow(6), 7)
        self.assertEqual(sn.getNextInRow(7), 8)
        self.assertEqual(sn.getNextInRow(8), None)

        self.assertEqual(sn.getPrevInRow(0), None)
        self.assertEqual(sn.getPrevInRow(1), 0)
        self.assertEqual(sn.getPrevInRow(2), 1)
        self.assertEqual(sn.getPrevInRow(3), None)
        self.assertEqual(sn.getPrevInRow(4), 3)
        self.assertEqual(sn.getPrevInRow(5), 4)
        self.assertEqual(sn.getPrevInRow(6), None)
        self.assertEqual(sn.getPrevInRow(7), 6)
        self.assertEqual(sn.getPrevInRow(8), 7)

        self.assertEqual(sn.getPrevInCol(0), None)
        self.assertEqual(sn.getPrevInCol(1), None)
        self.assertEqual(sn.getPrevInCol(2), None)
        self.assertEqual(sn.getPrevInCol(3), 0)
        self.assertEqual(sn.getPrevInCol(4), 1)
        self.assertEqual(sn.getPrevInCol(5), 2)
        self.assertEqual(sn.getPrevInCol(6), 3)
        self.assertEqual(sn.getPrevInCol(7), 4)
        self.assertEqual(sn.getPrevInCol(8), 5)

        self.assertEqual(sn.getNextInCol(0), 3)
        self.assertEqual(sn.getNextInCol(1), 4)
        self.assertEqual(sn.getNextInCol(2), 5)
        self.assertEqual(sn.getNextInCol(3), 6)
        self.assertEqual(sn.getNextInCol(4), 7)
        self.assertEqual(sn.getNextInCol(5), 8)
        self.assertEqual(sn.getNextInCol(6), None)
        self.assertEqual(sn.getNextInCol(7), None)
        self.assertEqual(sn.getNextInCol(8), None)

        self.assertEqual(sn.getToCor(0, 0), None)
        self.assertEqual(sn.getToCor(0, 2), None)
        self.assertEqual(sn.getToCor(0, 3), None)
        self.assertEqual(sn.getToCor(0, 4), 0)

        self.assertEqual(sn.getToCor(1, 2), None)
        self.assertEqual(sn.getToCor(1, 0), None)
        self.assertEqual(sn.getToCor(1, 5), None)
        self.assertEqual(sn.getToCor(1, 6), 4)

        self.assertEqual(sn.getToCor(2, 8), None)
        self.assertEqual(sn.getToCor(2, 6), None)
        self.assertEqual(sn.getToCor(2, 5), None)
        self.assertEqual(sn.getToCor(2, 4), 8)

        self.assertEqual(sn.getToCor(3, 6), None)
        self.assertEqual(sn.getToCor(3, 8), None)
        self.assertEqual(sn.getToCor(3, 3), None)
        self.assertEqual(sn.getToCor(3, 2), 4)

