import timeit
import numpy as np
import matplotlib.pyplot as plt

from linearsearch import find_parking_spot_linear, generate_random_parking_lot
from bitwiseoperation import find_parking_spot_bitwise

def benchmark_linear_search():
    parking_mask = generate_random_parking_lot()
    return timeit.timeit(lambda: find_parking_spot_linear(parking_mask), number=100000)

def benchmark_bitwise_operation():
    parking_mask = generate_random_parking_lot()
    return timeit.timeit(lambda: find_parking_spot_bitwise(parking_mask), number=100000)


def main():
    linear_search_times = [benchmark_linear_search() for _ in range(5)]
    bitwise_operation_times = [benchmark_bitwise_operation() for _ in range(5)]

    print("Below are the time complexity of each method after 5 times running:")
    print("Linear Search Times (seconds):", linear_search_times)
    print("Bitwise Operation Times (seconds):", bitwise_operation_times)

    print("\nAverage Time for Linear Search:", np.mean(linear_search_times), "seconds")
    print("Average Time for Bitwise Operation:", np.mean(bitwise_operation_times), "seconds")

    print("\nSo from the average time complexity, Bitwise Operation is more efficient than Linear Search")

    # Visualize the results
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
