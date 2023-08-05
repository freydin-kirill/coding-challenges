def SeatingStudents(arr):
    # Extract the total number of seats (K) from the first element of the input array
    K = int(arr[0])

    # Extract the list of reserved seats from the remaining elements of the input array
    reserved = [int(n) for n in arr[1:]]

    # If the number of reserved seats is equal to the total number of seats (K),
    # there are no available seats for students, so return 0.
    if len(reserved) == K:
        return 0

    # Initialize a variable to count the valid seating combinations
    combinations = 0

    # Loop through each seat from 1 to K
    for i in range(1, K + 1):
        # Skip the seat if it is reserved
        if i in reserved:
            continue

        # Calculate neighboring seats based on whether the seat number is even or odd
        if i % 2 != 0:  # If the seat number is odd
            neighboring = [i - 2, i + 1, i + 2]  # Neighboring seats are two seats back and one and two seats forward
        else:  # If the seat number is even
            neighboring = [i - 2, i - 1,
                           i + 2]  # Neighboring seats are two seats back, one seat back, and two seats forward

        # Check if each neighboring seat is valid (within the range 1 to K) and not reserved
        for j in neighboring:
            if j < 1 or K < j or j in reserved:
                continue
            combinations += 1  # Increment the combinations count for each valid neighboring seat

    # The total number of combinations counted includes symmetric combinations where seats
    # have been swapped (e.g., seat 1 and seat 2 are considered the same as seat 2 and seat 1).
    # So, we divide the total combinations by 2 to avoid counting symmetric combinations twice.
    return combinations // 2


# Keep this function call here
print(SeatingStudents(input()))
