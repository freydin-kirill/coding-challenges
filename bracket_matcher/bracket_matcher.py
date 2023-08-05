def BracketMatcher(strParam):
    # Initialize a counter to keep track of open parentheses '('
    brackets_counter = 0

    # Loop through each character in the input string
    for sym in strParam:
        # If an opening parenthesis is encountered, increment the counter
        if sym == '(':
            brackets_counter += 1

        # If a closing parenthesis is encountered, decrement the counter
        if sym == ')':
            brackets_counter -= 1

        # If the counter goes negative, it means there are more closing parentheses than
        # opening ones, which makes the parentheses unbalanced. So, return 0.
        if brackets_counter < 0:
            return 0

    # After processing the entire string, if the counter is 0, it means the parentheses are balanced.
    # Return 1 (True) indicating balanced parentheses, otherwise, return 0 (False).
    return 1 if brackets_counter == 0 else 0


# Keep this function call here
print(BracketMatcher(input()))
