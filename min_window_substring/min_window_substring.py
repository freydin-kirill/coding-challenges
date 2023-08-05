def MinWindowSubstring(strArr):
    # Separate the input into the main string and the pattern to find
    string, pattern = strArr

    # Initialize the minimum window length as the length of the pattern
    min_length = len(pattern)

    while True:
        # Iterate over all possible window lengths starting from min_length to the length of the main string
        for length in range(min_length, len(string) + 1):
            # Flag to track if the current window meets the condition of containing all characters of the pattern
            cond_is_met = True

            # Extract the substring of the current window
            substrings = string[length - min_length: length]

            # Check if all characters of the pattern are present in the current window and their counts match
            for char in set(list(pattern)):
                if char not in substrings or substrings.count(char) < pattern.count(char):
                    cond_is_met = False
                    break

            # If the condition is met, return the current window as it is the minimum window containing the pattern
            if cond_is_met:
                return substrings

        # If no window of length min_length contained the pattern, increase min_length to consider larger windows
        min_length += 1


# Keep this function call here
print(MinWindowSubstring(input()))
