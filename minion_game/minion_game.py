def minion_game(string):
    # Define the vowels that Kevin uses to form words
    vowels = 'AEIOU'
    
    # Initialize the scores for Stuart and Kevin to 0
    stuart_score, kevin_score = 0, 0
    
    # Loop through each character in the string and calculate scores for each player
    for i in range(len(string)):
        if string[i] in vowels:  # If the character is a vowel, Kevin gets points
            kevin_score += len(string) - i
        else:  # If the character is a consonant, Stuart gets points
            stuart_score += len(string) - i
    
    # Compare the scores and determine the winner
    if stuart_score > kevin_score:
        print("Stuart", stuart_score)
    elif kevin_score > stuart_score:
        print("Kevin", kevin_score)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
