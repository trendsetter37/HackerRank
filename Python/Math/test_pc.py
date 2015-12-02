import unittest
from polar_coord import polar_coord as pc


class TestPolarCoord(unittest.TestCase):
    def setUp(self):
        self.p_coords = ('1+2j', '-1+0j', '-1-5j', '1-1j')
        self.answers = (
            (2.2360679775, 1.10714871779),
            (1.0, 3.141592653589793),
            (5.09901951359, -1.76819188664),
            (1.41421356237, -0.785398163397)
        )

    def test_pc_function(self):
        for idx, test in enumerate(self.p_coords):
            distance, angle = pc(test)
            self.assertAlmostEqual(
                distance, self.answers[idx][0],
                places=3, msg='Incorrect distance'
            )
            self.assertAlmostEqual(
                angle, self.answers[idx][1],
                places=3, msg='Incorrect angle'
            )

if __name__ == '__main__':
    unittest.main()
