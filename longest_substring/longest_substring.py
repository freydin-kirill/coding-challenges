class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        # Create a dictionary to store the index of the last occurrence of each character seen
        seen = {}

        # Initialize two pointers: 'left' represents the left boundary of the current substring,
        # and 'length' stores the length of the longest substring found so far.
        left = 0
        length = 0

        # By using a sliding window approach we can reduce runtime to O(n)
        # Iterate through the characters of the string using the right pointer 'right'
        for right in range(len(string)):
            char = string[right]  # Get the character at the current position 'right'

            # Check if the character is already in the 'seen' dictionary and its last occurrence index is greater than or equal to 'left'
            # If it is, update 'left' to be the next index after the last occurrence of the character,
            # effectively skipping the substring that contains the repeated character.
            if char in seen and seen[char] >= left:
                left = seen[char] + 1
            else:
                # If the character is not in 'seen' or its last occurrence index is before 'left',
                # it means the character is unique in the current substring.
                # Calculate the length of the current substring and update 'length' if it is longer.
                length = max(length, right - left + 1)

            # Update the index of the last occurrence of the character in 'seen'
            seen[char] = right

        # Return the length of the longest substring without repeating characters
        return length
