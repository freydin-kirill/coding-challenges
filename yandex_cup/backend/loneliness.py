import numpy as np


def least_squares_location(coord):
    arr = np.array(
        [[2 * (beacon[0] - coord[0][0]), 2 * (beacon[1] - coord[0][1]), 2 * (beacon[2] - coord[0][2])] for
         beacon in coord])
    b = np.array([beacon[0] ** 2 - coord[0][0] ** 2 + beacon[1] ** 2 - coord[0][1] ** 2 + beacon[2] ** 2 -
                  coord[0][2] ** 2 + beacon[3] ** 2 - coord[0][3] ** 2 for beacon in coord])

    result, residuals, rank, singular_values = np.linalg.lstsq(arr, b, rcond=None)
    location = result / 2

    return location


if __name__ == '__main__':
    K = int(input())
    beacons = []
    for _ in range(K):
        beacon_data = list(map(float, input().split()))
        beacons.append(beacon_data)

    gregory = least_squares_location(beacons)
    print(f"{gregory[0]:.6f} {gregory[1]:.6f} {gregory[2]:.6f}")