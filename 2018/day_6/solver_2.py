import numpy as np
from scipy.spatial import distance
import string

np.set_printoptions(edgeitems=50)


def dist(point_a, point_b):
    d = distance.pdist(np.array([point_a, point_b]), 'cityblock')
    return d


with open("input.txt", "r") as data:
    coord = [a.split(', ') for a in data.read().splitlines()]
    coord = [[int(x), int(y)] for x, y in coord]
    print(coord)

    min_x = min(i[0] for i in coord)
    max_x = max(i[0] for i in coord)
    min_y = min(i[1] for i in coord)
    max_y = max(i[1] for i in coord)
    print("Area size: {} {} {} {}".format(min_x, max_x, min_y, max_y))

    matrix = np.empty((max_y - min_y + 1, max_x - min_x + 1), dtype='<U10')

    # move coordinates:
    coord = [[x-min_x, y-min_y] for x, y in coord]
    max_distance = 10000
    numbers_to_eliminate = []

    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            point_ok = True
            current_distance_sum = 0
            for index, coo in enumerate(coord):
                # print("Actual pos [{}, {}]dist to {} is {}".format(x, y, coo, dist_to_coo))
                dist_to_coo = dist([x, y], coo)
                current_distance_sum += int(dist_to_coo)
                if current_distance_sum >= max_distance:
                    point_ok = False
                    break

            # print("Distance for {} sum: {}".format((x, y), current_distance_sum))

            if point_ok:
                matrix[y, x] = str("o")
            else:
                matrix[y, x] = str("x")

    unique, counts = np.unique(matrix, return_counts=True)
    print("Eliminate: ")
    print("Unique: " + str(unique) + " " + str(counts))
