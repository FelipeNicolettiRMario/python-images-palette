from math import sqrt

def distance_3d_points(point_1 : tuple, point_2 : tuple) -> int:

    points_distance = sqrt(
        pow(point_2[0] - point_1[0],2) +
        pow(point_2[1] - point_1[1],2) +
        pow(point_2[2] - point_1[2],2) * 1.0
    )

    return points_distance
