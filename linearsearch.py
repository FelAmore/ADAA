import time
import random


def generate_random_parking_lot(size=10):
    # Generate a random binary string of 0s and 1s with the specified size
    binary_string = ''.join(random.choice('01') for _ in range(size))
    # Convert the binary string to an integer using base 2 (binary)
    return int(binary_string, 2)


def find_parking_spot_linear(bitmask):
    # Iterate through each bit position in the bitmask from right to left
    for i in range(len(bin(bitmask)) - 2):
        if not (bitmask & (1 << i)): # Check if the bit at the current position is not set (0)
            return i # Return the position of the leftmost available parking spot
    return -1  # If no available parking spots are found, return -1


def print_parking_lot_status(bitmask, size=10):
    binary_representation = bin(bitmask)[2:] # Convert the bitmask to its binary representation and remove the '0b' prefix
    binary_representation = binary_representation.rjust(size, '0')  # Pad the binary representation with leading zeros to match the specified size

    # Iterate through each bit in the reversed binary representation
    for bit in reversed(binary_representation):
        if bit == '0':
            print('🟢', end=' ')  # Green for unoccupied
        else:
            print('🚗', end=' ')  # Red for occupied
    print()
    print(' 0  1  2  3  4  5  6  7  8  9') # Labeling each parking spot


def main():
    # Dummy data for testing
    parking_mask = generate_random_parking_lot()

    # Print the initial parking lot status
    print("Initial Parking Lot Status:")
    print_parking_lot_status(parking_mask)

    # Find a parking spot using linear search
    start_time = time.time()
    parking_spot = find_parking_spot_linear(parking_mask)
    end_time = time.time()

    # Check if a parking spot is found
    if parking_spot != -1:
        # Print the position of the found parking spot
        print(f"Found available parking spot at position {parking_spot}.")
        # Update the bitmask to mark the spot as occupied
        parking_mask |= (1 << parking_spot)
        # Print the updated parking lot status
        print("Updated Parking Lot Status:")
        print_parking_lot_status(parking_mask)
    else:
        # Print a message if no available parking spots are found
        print("No available parking spots.")

    # Calculate and print the time complexity
    time_complexity = end_time - start_time
    print(f"Time complexity: {time_complexity} seconds")


if __name__ == "__main__":
    main()



