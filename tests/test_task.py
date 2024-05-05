import unittest
from unittest.mock import patch, mock_open
from common.tk_drawer import TkDrawer
from shadow.polyedr import Polyedr


class TestPolyedr(unittest.TestCase):
    def setUp(self) -> None:
        self.tk = TkDrawer()

    def test_length1(self):
        p = Polyedr("data/test1.geom")
        p.draw(self.tk)
        self.assertEqual(p.X, 0)

    def test_length2(self):
        p = Polyedr("data/test2.geom")
        p.draw(self.tk)
        self.assertEqual(p.X, 0)

    def test_length3(self):
        p = Polyedr("data/test3.geom")
        p.draw(self.tk)
        self.assertAlmostEqual(p.X, 4)

    def test_length4(self):
        p = Polyedr("data/test4.geom")
        p.draw(self.tk)
        self.assertAlmostEqual(p.X, 2)

    def test_length5(self):
        p = Polyedr("data/test5.geom")
        p.draw(self.tk)
        self.assertAlmostEqual(p.X, 7)
