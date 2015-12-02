''' Testing right angle class '''

import unittest
from find_angle_mbc import RightTriangle  # pylint: disable-msg=F0401


class TestRightTriangle(unittest.TestCase):  # pylint: disable-msg=R0904
    ''' Used to test RightTriangle class '''
    def setUp(self):
        ''' side, side, answer, hypot, small_hypot, far_angle, adj_side'''
        self.test_cases = (
            (10, 10, 45),
            (56, 54, 46),
            (1, 100, 1),
            (1, 10, 6)
        )

    def test_target_angle(self):
        ''' Test for correct target_angle property '''
        for test in self.test_cases:
            triangle = RightTriangle(test[0], test[1])
            self.assertEqual(test[2], triangle.angle_mbc)
        del triangle


if __name__ == '__main__':
    unittest.main()
