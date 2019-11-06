import math


def cubeVolume(a):  # take one input s(side length) to calculate the volume of a cube
    volume = a ** 3
    return round(volume, 2)


def pyramidVolume(b,h):  # take two inputs b(base) and h(height) to calculate the  volume of a pyramid
    volume = (1/3)*(b ** 2)*h
    return round(volume, 2)


def ellipsoidVolume(r1, r2, r3):  # take three inputs r1, r2, and r3 to calculate the volume of an ellipsoid
    volume = ((4/3)*math.pi)*r1*r2*r3
    return round(volume, 2)




























