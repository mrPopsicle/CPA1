# Description: This file contains the code for the main menu for High School Math Question
import SEQUENCES_MENU
import Trigonometry_Menu
import Algebra_Menu



def math_practice_highschool():
    """Main menu to select a topic for high school math."""
    score = 0
    streak = 0
    
    print("\n Welcome to the High School Math Practice Program!")

    while True:
        print("\nSelect a topic:")
        print("1. Sequences")
        print("2. Algebra")
        print("3. Trigonometry")
        print("4. Exit")
        

        choice = input("Enter your choice: ")

        if choice == '1':
            print("You selected Sequences...\n")
            score, streak = SEQUENCES_MENU.sequences_menu(score, streak)
        elif choice == '2':
            print("You selected Algebra...\n")
            score, streak = Algebra_Menu.algebra_menu(score, streak)   
        elif choice == '3':
            print("You selected Trigonometry...\n")
            score, streak = Trigonometry_Menu.trigonometry_menu(score, streak)
        elif choice == '4':
            print("Thank you for playing! Your final score is {score}. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.\n")

def get_user_input():
    """Get user input and return the value. Accepts integers, floats,"""
    user_input = input("Enter your answer: ")

    
    try:
        return int(user_input)
    except ValueError:
        pass

    try:
        return float(user_input)
    except ValueError:
        pass

    
    return user_input

def update_score(correct, streak, score):
    """Updates score based on streak"""
    points = 10
    if streak > 1:
        points *= 2
    if correct:
        score += points
        streak += 1
    else:
        streak = 0
    return score, streak


if __name__ == "__main__":
    math_practice_highschool()
