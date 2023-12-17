import time
import numpy as np
import matplotlib.pyplot as plt

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

    print("Below are the time complexity of each method after 5 times running:")
    print("Linear Search Times (seconds):", linear_search_times)
    print("Bitwise Operation Times (seconds):", bitwise_operation_times)

    print("\nAverage Time for Linear Search:", np.mean(linear_search_times), "seconds")
    print("Average Time for Bitwise Operation:", np.mean(bitwise_operation_times), "seconds")

    print("\nSo from the average time complexity, Bitwise Operation is more efficient than Linear Search")

    # Visualize the results in graph form
    labels = ['Trial 1', 'Trial 2', 'Trial 3', 'Trial 4', 'Trial 5']
    plt.plot(labels, linear_search_times, label='Linear Search')
    plt.plot(labels, bitwise_operation_times, label='Bitwise Operation')
    plt.xlabel('Trial')
    plt.ylabel('Average Time (seconds)')
    plt.title('Comparison of Time Complexity')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()

