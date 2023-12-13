import time
import random

def find_parking_spot_bitwise(bitmask):
    available_spots = [i for i in range(len(bin(bitmask)) - 2) if not (bitmask & (1 << i))]
    if available_spots:
        return random.choice(available_spots)
    else:
        return -1  # No available parking spots

def print_parking_lot_status(bitmask):
    binary_representation = bin(bitmask)[2:]  # Convert to binary and remove the '0b' prefix
    for bit in binary_representation:
        if bit == '0':
            print('\033[92m' + 'G' + '\033[0m', end=' ')  # Green for unoccupied
        else:
            print('\033[91m' + 'R' + '\033[0m', end=' ')  # Red for occupied
    print()

def main():
    # Dummy data for testing
    parking_lot_size = 10
    parking_mask = int('1010010110', 2)  # Binary representation where 0 represents an available spot

    print("Initial Parking Lot Status:")
    print_parking_lot_status(parking_mask)

    # Find a parking spot
    start_time = time.time()
    parking_spot = find_parking_spot_bitwise(parking_mask)
    end_time = time.time()

    if parking_spot != -1:
        print(f"Found available parking spot at position {parking_spot}.")
        # Update the bitmask to mark the spot as occupied
        parking_mask |= (1 << parking_spot)
        print("Updated Parking Lot Status:")
        print_parking_lot_status(parking_mask)
    else:
        print("No available parking spots.")

    # Calculate and print the time complexity
    time_complexity = end_time - start_time
    print(f"Time complexity: {time_complexity} seconds")

if __name__ == "__main__":
    main()