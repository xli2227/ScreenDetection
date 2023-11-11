from get_coords import *
from exeution import *
import time


def main():
    coordinates = get_coords()
    print(coordinates)
    while True:
        start = time.perf_counter()
        detection_and_alarm(coordinates[0][0], coordinates[0][1], coordinates[1][0], coordinates[1][1])
        latency = time.perf_counter() - start
        print('======= Finish Iteration ======== with latency ', latency)

if __name__ == "__main__":
    main()