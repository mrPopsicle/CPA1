"""This file contains the code for the submenu for Trigonometry."""
# Importing the necessary modules for the program.
import Trigonometric_Questions
from CPA1_HS_SECTION2 import get_user_input, update_score

def trigonometry_menu(score, streak):
    """Main menu for trigonometry topics."""
    print("\nWelcome to the Trigonometry Quiz Section!")

    while True:
        print("\nSelect a topic:")
        print("1. Unit Circle")
        print("2. Inverse Trigonometry")
        print("3. Right Triangle")
        print("4. Exit")

        choice = input("Enter the number of the topic you would like to practice: ")
        if choice not in ("1", "2", "3"):
            print("Invalid choice. Please select a valid option.\n")
            continue
        if choice == "4":
            print(f"Exiting Trigonometry section. Your final score is {score}. Goodbye")
            break

        while True:
            if choice == "1":
                print("You selected Unit Circle. Starting quiz...\n")
                correct_answer = Trigonometric_Questions.unit_circle()
                user_answer = get_user_input()
                while user_answer != correct_answer:
                    print("Incorrect. Try again.")
                    user_answer = get_user_input()
                print("Correct!\n")
                score, streak = update_score(True, streak, score)
                
            elif choice == "2":
                print("You selected Inverse Trigonometry. Starting quiz...\n")
                correct_answer = Trigonometric_Questions.inverse_trig()
                user_answer = get_user_input()
                while user_answer != correct_answer:
                    print("Incorrect. Try again.")
                    user_answer = get_user_input()
                print("Correct!\n")
                score, streak = update_score(True, streak, score)
                
            elif choice == "3":
                print("You selected Right Triangle. Starting quiz...\n")
                correct_answer = Trigonometric_Questions.right_triangle()
                user_answer = get_user_input()
                while user_answer != correct_answer:
                    print("Incorrect. Try again.")
                    user_answer = get_user_input()
                print("Correct!\n")
                score, streak = update_score(True, streak, score)
    
            repeat = input("Practice this topic again? (y/n): ").strip().lower()
            if repeat == "y":
                continue
            else:
                break
    return score, streak

    
if __name__ == "__main__":
    score, streak = 0, 0
    trigonometry_menu(score, streak)
