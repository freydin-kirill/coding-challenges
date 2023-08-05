# Import the product function from itertools module to compute Cartesian product
from itertools import product

# Main program
if __name__ == '__main__':
    # Read K (the number of lists) and M (modulo value) from the user
    K, M = map(int, input().split())

    # Read data for each list and compute the squares of elements
    data = [list(map(lambda x: int(x)**2, input().split()))[1:] for _ in range(K)]

    # Compute the Cartesian product of elements from each list and calculate the sum of squares modulo M
    results = list(map(lambda x: sum(x) % M, product(*data)))

    # Print the maximum result obtained from the sums
    print(max(results))
