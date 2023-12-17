import timeit
import numpy as np
import matplotlib.pyplot as plt

from linearsearch import find_parking_spot_linear, generate_random_parking_lot
from bitwiseoperation import find_parking_spot_bitwise

def benchmark_linear_search():
    # Generate a random parking lot status for testing
    parking_mask = generate_random_parking_lot()
    # Measure execution time of find_parking_spot_linear using timeit.
    # Lambda calls the function with the generated parking_mask; adjust the 'number' parameter.
    return timeit.timeit(lambda: find_parking_spot_linear(parking_mask), number=100000)

def benchmark_bitwise_operation():
    # Generate a random parking lot status for testing
    parking_mask = generate_random_parking_lot()
    # Measure execution time of find_parking_spot_bitwise using timeit.
    # Lambda calls the function with the generated parking_mask; adjust the 'number' parameter.
    return timeit.timeit(lambda: find_parking_spot_bitwise(parking_mask), number=100000)


def main():
    # Measure the time complexity of linear search and bitwise operation for 5 trials
    linear_search_times = [benchmark_linear_search() for _ in range(5)]
    bitwise_operation_times = [benchmark_bitwise_operation() for _ in range(5)]

    # Display the time complexity results for each method after five times running
    print("Below are the time complexity of each method after 5 times running:")
    print("Linear Search Times (seconds):", linear_search_times)
    print("Bitwise Operation Times (seconds):", bitwise_operation_times)

    # Calculate and display the average time complexity for each method
    linearsearch_mean = np.mean(linear_search_times)
    bitwiseoperation_mean = np.mean(bitwise_operation_times)
    print("\nAverage Time for Linear Search:", linearsearch_mean, "seconds")
    print("Average Time for Bitwise Operation:", bitwiseoperation_mean, "seconds")

    if linearsearch_mean < bitwiseoperation_mean:
        faster = 'Linear Search'
        slower = 'Bitwise Operation'
    else:
        faster = 'Bitwise Operation'
        slower = 'Linear Search'
    print(f"\nSo from the average time complexity, {faster} is more efficient than {slower}")

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
