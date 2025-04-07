"""
This module contains functions to generate and display different types of sequences
and quizzes the user on them. It includes the arithmetic, geometric, harmonic, and Fibonacci sequences.
It also provides a menu for the user to select which type of sequence they want to practice.
"""
import random
from CPA1_HS_SECTION2 import get_user_input, update_score

def arithmetic_sequence():
    """generate an arithmetic sequence question"""
    start = random.randint(-10, 20)
    diff = random.randint(1, 10)
    length = random.randint(5, 10)
    sequence = []
    for i in range(length):
        sequence.append(start + i * diff)
    print(f"\nWhat is the next term in this sequence?\n{sequence}")
    next_term = sequence[-1] + diff
    return next_term

def geometric_sequence():
    """generate a geometric sequence question"""
    start = random.randint(1, 10)
    ratio = random.randint(2, 5)
    length = random.randint(5, 10)
    sequence = []
    for i in range(length):
        sequence.append(start * ratio ** i)
    print(f"\nWhat is the next term in this sequence?\n{sequence}")
    next_term = start * ratio ** length
    return next_term

def harmonic_sequence():
    """generate a harmonic sequence question"""
    start = random.randint(1, 10)
    diff = random.randint(1, 5)
    length = random.randint(5, 10)
    sequence = []
    for i in range(length):
        sequence.append(1 / (start + i * diff))
    print(f"\nWhat is the next term in this sequence?\n{sequence}")
    next_term = 1 / (start + length * diff)
    return next_term

def fibonacci_sequence():
    """generate a fibonacci sequence question"""
    sequence = [0, 1, 1, 2, 3]
    length = random.randint(7, 50)
    for i in range(2, length):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    print(f"\nWhat is the next term in this sequence?\n{sequence}")
    next_term = sequence[-1] + sequence[-2]
    return next_term
        
def sequences_menu(score, streak):
    """Main menu for sequence topics."""
    print("\nWelcome to the Sequences Section!")

    while True:
        print("\nSelect a topic:")
        print("1. Arithmetic Sequences")
        print("2. Geometric Sequences")
        print("3. Harmonic Sequences")
        print("4. Fibonacci Sequences")
        print("5. Exit")

        choice = input("Enter the number of the topic you would like to practice: ")
        while True:
            if choice == "1":
                print("You selected Arithmetic Sequences. Starting quiz...\n")
                correct_answer = arithmetic_sequence()
                user_answer = get_user_input()
                while user_answer != correct_answer:
                    print("Incorrect. Try again.")
                    user_answer = get_user_input()
                print("Correct!\n")
                score, streak = update_score(True, streak, score)
            elif choice == "2":
                print("You selected Geometric Sequences. Starting quiz...\n")
                correct_answer == geometric_sequence()
                user_answer = get_user_input()
                while user_answer != correct_answer:
                    print("Incorrect. Try again.")
                    user_answer = get_user_input()
                print("Correct!\n")
                score, streak = update_score(True, streak, score)
            elif choice == "3":
                print("You selected Harmonic Sequences. Starting quiz...\n")
                correct_answer == harmonic_sequence()
                user_answer = get_user_input()
                while user_answer != correct_answer:
                    print("Incorrect. Try again.")
                    user_answer = get_user_input()
                print("Correct!\n")
                score, streak = update_score(True, streak, score)
            elif choice == "4":
                print("You selected Fibonacci Sequences. Starting quiz...\n")
                fibonacci_sequence()
                user_answer = get_user_input()
                while user_answer != correct_answer:
                    print("Incorrect. Try again.")
                    user_answer = get_user_input()
                print("Correct!\n")
                score, streak = update_score(True, streak, score)
            elif choice == "5":
                print("Thank you for playing! Your final score is {score}. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.\n")
    
            repeat = input("Practice this topic again? (y/n): ").strip().lower()
            if repeat == "y":
                continue
            else:
                break
                
        return score, streak

if __name__ == "__main__":
    score, streak = 0, 0
    sequences_menu()

