"""
Number Guessing Game (CLI)
Features:
- Randomly chooses a number
- Higher/lower hints
- Difficulty levels (easy/medium/hard)
- Replay option and best score tracking (in-memory)
"""
import random

def choose_number(difficulty):
    ranges = {'easy': 10, 'medium': 50, 'hard': 100}
    return random.randint(1, ranges.get(difficulty, 50)), ranges.get(difficulty, 50)

def play_round(difficulty):
    number, top = choose_number(difficulty)
    attempts = 0
    print(f"Guess the number between 1 and {top}")
    while True:
        attempts += 1
        try:
            guess = int(input("Your guess: ").strip())
        except ValueError:
            print("Please enter an integer.")
            continue
        if guess == number:
            print(f"Correct! Attempts: {attempts}")
            return attempts
        elif guess < number:
            print("Higher.")
        else:
            print("Lower.")

def menu():
    best_scores = {'easy': None, 'medium': None, 'hard': None}
    while True:
        print("\nNumber Guessing Game")
        diff = input("Choose difficulty (easy/medium/hard) or 'exit': ").strip().lower()
        if diff == 'exit':
            print("Thanks for playing!")
            return
        if diff not in ('easy','medium','hard'):
            print("Invalid difficulty.")
            continue
        attempts = play_round(diff)
        if best_scores[diff] is None or attempts < best_scores[diff]:
            best_scores[diff] = attempts
            print(f"New best for {diff}: {attempts}")
        print("Best scores:", best_scores)
        again = input("Play again? (y/n): ").strip().lower()
        if again != 'y':
            print("Exiting game.")
            return

if __name__ == '__main__':
    menu()
