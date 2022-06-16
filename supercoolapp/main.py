import random
import math

from .mylocalutil import MYCONSTANT


def generate_points(rows=4, cols=4) -> list[(int, int)]:
    result: list[(int, int)] = []
    for r in range(rows):
        for c in range(cols):
            val = random.randint(0, 1)
            if val == 1:
                result.append((r, c))

    return result


def bottom_left_most_point(points: list[(int, int)]):
    p = None
    for point in points:
        if not p or (point[0] <= p[0] and point[1] <= p[1]):
            p = point
    return p


def slope(point_a: (int, int), point_b: (int, int)):
    a_x, a_y = point_a
    b_x, b_y = point_b
    return (b_x - a_x) / (b_y - b_x) if (b_y - b_x) != 0 else math.inf


def main():
    print("running main()")
    print("MYCONSTANT", MYCONSTANT)
    points = generate_points()

    print("points", points)

    bottom_leftmost = bottom_left_most_point(points)
    print("bottom_left_most_point", bottom_leftmost)

    for point in points:
        if point != bottom_leftmost:
            print("slope", point, slope(bottom_leftmost, point))


if __name__ == "__main__":
    print("__name__==__main__")
    main()
