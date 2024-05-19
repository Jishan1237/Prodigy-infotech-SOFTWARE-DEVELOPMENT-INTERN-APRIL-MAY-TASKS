import random

def calculate_score(attempts):
    base_score = 100  # Base score for correct guess
    score_deduction = 10 * (5 - attempts)  # Score deduction for each wrong attempt
    return max(0, base_score - score_deduction)  # Ensure score is non-negative

def guess_the_number():
    min_number = 1
    max_number = 100
    total_rounds = 3  # Let's play 3 rounds
    current_round = 0
    total_attempts = 0  # Total attempts across all rounds
    total_score = 0  # Total score across all rounds
    play_again = True

    # Welcome message and game instructions
    print("Welcome to Guess the Number Game!")
    user_attempts = int(input("How many attempts do you want for each round? "))

    while play_again and current_round < total_rounds:
        current_round += 1
        print(f"\nRound {current_round}:")
        attempts = 0
        total_attempts += user_attempts  # Increment total attempts
        print(f"You have {user_attempts} attempts to guess the correct number.")
        random_number = random.randint(min_number, max_number)
        print(f"Guess the number between {min_number} and {max_number}:")

        guessed_correctly = False

        while not guessed_correctly and attempts < user_attempts:
            attempts += 1
            guessed_number = int(input())

            if guessed_number == random_number:
                print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
                guessed_correctly = True
                round_score = calculate_score(attempts)
                total_score += round_score  # Increment total score
                print(f"Round {current_round} Score: {round_score}")
            elif guessed_number < random_number:
                print("Try again! The number is higher.")
            else:
                print("Try again! The number is lower.")

        if not guessed_correctly:
            print(f"Out of attempts! The correct number was: {random_number}")

        print(f"Total Attempts so far: {total_attempts}")
        print(f"Total Score so far: {total_score}")
        play_next_round_response = input("Do you want to play the next round? (yes/no) ")

        if play_next_round_response.lower() != "yes":
            play_again = False

    # Display final score and thank you message
    print(f"\nFinal Score: {total_score}")
    print("Thanks for playing!")

if __name__ == "__main__":
    guess_the_number()
