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
    print(coord)

    print(matrix)

    numbers_to_eliminate = []

    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            # print('\n')
            best_dist = max(matrix.shape)*2
            winner = ''
            count = 0
            for index, coo in enumerate(coord):
                dist_to_coo = dist([x, y], coo)
                # print("Actual pos [{}, {}]dist to {} is {}".format(x, y, coo, dist_to_coo))
                if dist_to_coo == 0:
                    # print("Change winner:" + str(index))
                    winner = str(index)
                    count = 0
                    break
                if dist_to_coo < best_dist:
                    best_dist = dist_to_coo
                    count = 1
                    # print("Change winner:" + str(index))
                    winner = str(index)
                elif dist_to_coo == best_dist and dist_to_coo != 0:
                    count += 1

            if count > 1:
                # print("setting tne .")
                winner = "."

            # print("Set winner: " + str(winner))
            if x == 0 or x == len(matrix[0]) - 1 or y == 0 or y == len(matrix) - 1:
                numbers_to_eliminate.append(str(winner))
                numbers_to_eliminate = list(set(numbers_to_eliminate))

            matrix[y, x] = str(winner)
            # print("Which results: " + str(matrix[y, x]))

    unique, counts = np.unique(matrix, return_counts=True)
    print("Eliminate: ")
    print(numbers_to_eliminate)
    uniq = np.asarray((unique, counts))
    uniq2 = []
    numbers_to_consider = set(uniq[0]) - set(numbers_to_eliminate)
    for i, c in enumerate(uniq[0]):
        if c in numbers_to_consider:
            uniq2.append((c, int(uniq[1][i])))
    print("Remain pairs:" + str(uniq2))
    uniq2 = np.array(uniq2).T
    print("Number to consider: " + str(numbers_to_consider))
    print("Remain pairs:" + str(uniq2))
    print("Sum: " + str(sum(counts)))
    print("should be: " + str((max_y - min_y + 1)*(max_x - min_x + 1)))
    print("Look thru: " + str([int(i) for i in uniq2[1]]))
    print(max([int(i) for i in uniq2[1]]))
