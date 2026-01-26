import math


def square(side):
    side_rounded = math.ceil(side)
    return side_rounded ** 2


side_length = math.exp(321)
area = square(side_length)
print(f"Площадь квадрата со стороной {side_length} \
     (округленной вверх): {area}")
