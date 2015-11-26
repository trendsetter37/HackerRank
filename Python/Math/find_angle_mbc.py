''' Module doctstring '''


import math


class RightTriangle(object):  #pylint: disable-msg=R0903
    ''' Incomplete Need to refactor '''
    main_angle = 90  # degrees / right triangle

    def __init__(self, side_AB, side_BC):
        self.side_ab = float(side_AB)
        self.side_bc = float(side_BC)

    @property
    def angle_mbc(self):
        ''' returns missing angle '''
        return round(math.degrees(math.atan(self.side_ab / self.side_bc)))

if __name__ == '__main__':
    SIDE1, SIDE2 = int(raw_input()), int(raw_input())
    TRI = RightTriangle(SIDE1, SIDE2)
    print str(TRI.angle_mbc) + u'\u00b0'
