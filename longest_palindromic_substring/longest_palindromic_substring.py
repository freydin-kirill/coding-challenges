class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Check if the entire input string 's' is already a palindrome
        # If it is, return the entire string as the longest palindrome
        if s == s[::-1]:
            return s

        # Initialize 'start' to store the starting index of the longest palindrome substring found so far,
        # and 'size' to store the length of the longest palindrome substring found so far (initially set to 1)
        start, size = 0, 1

        # Loop through the characters of the input string 's' from the second character (index 1)
        for i in range(1, len(s)):
            # Calculate the left and right indices for two substrings: s1 and s2
            left, right = i - size, i + 1
            s1, s2 = s[left - 1:right], s[left:right]

            # Check if s1 (substring ending at index i) is a palindrome
            if left >= 1 and s1 == s1[::-1]:
                size += 2
                start = left - 1  # Update the starting index of the longest palindrome
            # Check if s2 (substring ending at index i) is a palindrome
            elif s2 == s2[::-1]:
                size += 1
                start = left  # Update the starting index of the longest palindrome

        # Return the longest palindrome substring found based on the 'start' and 'size' values
        return s[start: start + size]
