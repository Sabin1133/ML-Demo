def comp_sign(a, b):
    return 1 if a > b else -1 if a < b else 0


def manhattan_dist(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])

