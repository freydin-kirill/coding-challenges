#!/bin/python3

# Import the 're' module for regular expression operations (used later in the code)
import re

# Read the first line of input, which contains two space-separated integers n and m
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])  # n represents the number of rows in the matrix
m = int(first_multiple_input[1])  # m represents the number of columns in the matrix

# Initialize an empty matrix to store the input data
matrix = []

# Read the next n lines of input, which contain the matrix data, and store them in the 'matrix' list
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

# Decode the script based on the provided logic

# Step 1: Construct the decoded script by joining characters from the matrix
# The decoded script is obtained by traversing the matrix in a zigzag manner
decoded_script = ''.join(matrix[k % n][k // n] for k in range(n * m))

# Step 2: Perform a regular expression substitution to remove unnecessary spaces in the decoded script
# The regular expression finds spaces between two alphanumeric characters and replaces them with a single space
decoded_script = re.sub(r'(?<=\w)\W+(?=\w)', ' ', decoded_script)

# Step 3: Print the final decoded script
print(decoded_script)
