# Recursive function to guess the number
def computer_guess_recursive(low, high):
    # Base case: when low exceeds high (this is unlikely to happen)
    if low > high:
        print("Something went wrong. Please check the input.")
        return
    
    # Computer's guess is the midpoint of low and high
    guess = (low + high) // 2
    feedback = input(f"Is {guess} too high (h), too low (l), or correct (c)? ").lower()
    
    # Base condition: if the guess is correct
    if feedback == 'c':
        print(f"Yay! The computer guessed your number, {guess}, correctly!")
        return  # End the recursion

    # Recursive step: adjust range based on feedback
    elif feedback == 'h':
        # Guess was too high, search in the lower half
        computer_guess_recursive(low, guess - 1)
    elif feedback == 'l':
        # Guess was too low, search in the upper half
        computer_guess_recursive(guess + 1, high)
    else:
        print("Invalid input! Please respond with 'h', 'l', or 'c'.")
        computer_guess_recursive(low, high)  # Continue with the current range

# Function to start the game and handle the range input
def start_guessing_game():
    low = int(input("Enter the lower bound of the range: "))
    high = int(input("Enter the upper bound of the range: "))
    computer_guess_recursive(low, high)

# Start the game
start_guessing_game()
