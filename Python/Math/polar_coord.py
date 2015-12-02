import cmath


def polar_coord(complex_z):
    ''' complex is in the form of z = x + yj '''
    c_num = complex(complex_z)
    return abs(c_num), cmath.phase(c_num)
