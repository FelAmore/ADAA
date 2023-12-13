import time
import numpy as np

def find_parking_spot_linear(bitmask):
    for i in range(len(bin(bitmask)) - 2):  # Subtract 2 to exclude the '0b' prefix in binary representation
        if not (bitmask & (1 << i)):
            return i  # Found an available parking spot
    return -1  # No available parking spots

def find_parking_spot_bitwise(bitmask):
    if bitmask == 0:
        return -1  # No available parking spots

    position = 0
    while bitmask & (1 << position):
        position += 1

    return position

def benchmark_linear_search():
    total_time = 0
    for _ in range(5):
        start_time = time.time()
        find_parking_spot_linear(0b1010010110)
        end_time = time.time()
        total_time += (end_time - start_time)
    return total_time / 5

def benchmark_bitwise_operation():
    total_time = 0
    for _ in range(5):
        start_time = time.time()
        find_parking_spot_bitwise(0b1010010110)
        end_time = time.time()
        total_time += (end_time - start_time)
    return total_time / 5

def main():
    linear_search_times = [benchmark_linear_search() for _ in range(5)]
    bitwise_operation_times = [benchmark_bitwise_operation() for _ in range(5)]

    print("Average Time for Linear Search:", np.mean(linear_search_times), "seconds")
    print("Average Time for Bitwise Operation:", np.mean(bitwise_operation_times), "seconds")

    print("\nLinear Search Times (seconds):", linear_search_times)
    print("Bitwise Operation Times (seconds):", bitwise_operation_times)

if __name__ == "__main__":
    main()

