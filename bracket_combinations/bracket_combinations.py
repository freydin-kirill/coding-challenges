def CreateBracket(max_count: int, brackets: str, combinations: list):
    # Check if the count of open parentheses '(' is less than the desired max_count.
    # If yes, recursively call the CreateBracket function by adding an open parenthesis.
    if brackets.count('(') < max_count:
        CreateBracket(max_count, brackets + '(', combinations)

    # Check if the count of open parentheses '(' is greater than the count of closing parentheses ')'
    # and the count of closing parentheses is less than the desired max_count.
    # If yes, recursively call the CreateBracket function by adding a closing parenthesis.
    if brackets.count('(') > brackets.count(')') and brackets.count(')') < max_count:
        CreateBracket(max_count, brackets + ')', combinations)

    # If the length of the brackets string reaches 2 * max_count, it means a valid combination is formed.
    # Append this combination to the list of combinations.
    if len(brackets) == 2 * max_count:
        combinations.append(brackets)
        return


def BracketCombinations(num: int):
    # If the input number num is 0, it is a special case where there is only one valid combination, an empty string.
    if num == 0:
        return 1

    # Initialize an empty list to store all possible combinations of brackets.
    combinations = []

    # Call the CreateBracket function to generate all valid combinations of brackets.
    # The function will modify the 'combinations' list with all valid combinations.
    CreateBracket(num, '', combinations)

    # Return the number of valid combinations by returning the length of the 'combinations' list.
    return len(combinations)


# Keep this function call here
print(BracketCombinations(input()))
