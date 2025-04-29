def word_guessing_game(target_word):
    """
    Simulates a word guessing game where each letter must be guessed correctly.
    
    Args:
        target_word: The word to be guessed
        
    Returns:
        None (prints the guessing process)
    """
    # Convert to lowercase for easier comparison
    target_word = target_word.lower()
    current_guess = ""
    
    print("Word guessing game started!")
    print(f"Target word has {len(target_word)} letters.")
    
    # Iterate through each position in the target word
    for position in range(len(target_word)):
        target_letter = target_word[position]
        correct_guess = False
        
        # Continue until the correct letter is guessed
        while not correct_guess:
            guess = input(f"Guess letter at position {position}: ").lower()
            
            # Handle empty input
            if not guess:
                print("Please enter a letter.")
                continue
                
            # Take only the first character if multiple are entered
            guess = guess[0]
            
            if guess == target_letter:
                current_guess += guess
                print(f"Correct! Current progress: {current_guess}")
                correct_guess = True
            else:
                print("Try again.")
    
    print(f"Congratulations! You've guessed the word: {target_word}")
    return