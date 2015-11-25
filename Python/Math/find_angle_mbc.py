#!/usr/bin/env
# -*- coding: utf-8 -*-
import math


class RightTriangle(object):
    ''' Incomplete Need to refactor '''
    main_angle = 90  # degrees / right triangle

    def __init__(self, side_AB, side_BC):
        self.side_ab = side_AB
        self.side_bc = side_BC

    @property
    def hypot(self):
        return math.sqrt(self.side_ab**2 + self.side_bc**2)

    @property
    def small_hypot(self):
        return self.hypot / 2

    @property
    def far_angle(self):
        ''' Do not convert to radians just yet '''
        return math.asin(self.side_bc / self.hypot)

    @property
    def adj_side(self):
        return math.sqrt((self.side_bc**2 + self.small_hypot**2) - \
        (2 * self.side_bc * self.small_hypot * math.cos(self.far_angle)))

    @property
    def target_angle(self):
        return int(round(
            math.degrees(
                math.acos(
                    (self.small_hypot**2 - \
                    (self.adj_side**2 + self.side_bc**2)) / \
                    (-2 * self.side_bc * self.adj_side)
                    )
                )
            )
        )

if __name__ == '__main__':
    side1, side2 = int(raw_input()), int(raw_input())
    tri = RightTriangle(side1, side2)
    print str(tri.target_angle) + u'\u00b0'
