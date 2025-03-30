# Description: This file contains the code for the main menu for High School Math Question



def math_practice_highschool():
    """Main menu to select a topic for high school math."""
    print("\n🎓 Welcome to the High School Math Practice Program!")

    while True:
        print("\nSelect a topic:")
        print("1. Sequences")
        print("2. Algebra")
        print("3. Trigonometry")
        print("4. Exit")
        

        choice = input("Enter your choice: ")

        

def get_user_input():
    """Get user input and return the value. Accepts integers, floats, and strings."""
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


if __name__ == "__main__":
    math_practice_highschool()
