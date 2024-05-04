import unittest
from unittest.mock import patch, mock_open
from shadow.polyedr import Polyedr


class TestPolyedr(unittest.TestCase):
    def test_length1(self):
        self.assertAlmostEqual(Polyedr("/data/test1.geom").X, )
