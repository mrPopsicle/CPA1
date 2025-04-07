"""This file contains the code for the submenu for Trigonometry."""

import random
import math
from fractions import Fraction
import Trigonometric_Questions

def right_triangles():
    """Quiz on right triangle calculations."""
    a = random.randint(3, 10)
    b = random.randint(3, 10)
    
    print(f"\nGiven a right triangle with a = {a} and b = {b}")
    print("What is the hypotenuse (c)?")
    
    input("Your answer: ")
    c = math.sqrt(a ** 2 + b ** 2)
    print(f"Correct answer: {round(c, 2)}")


def trigonometric_identities():
    """Quiz on basic trig identities"""
    questions = [
        {
            "question": "Which of the following is a true identity?",
            "options": [
                "1. sin²(x) + cos²(x) = 1",
                "2. sin(x) * cos(x) = 1",
                "3. tan(x) = sin(x) + cos(x)",
                "4. cos(x) = 1 / sin(x)"
            ],
            "answer": "1"
        },
        {
            "question": "What is tan(x) equal to?",
            "options": [
                "1. sin(x) * cos(x)",
                "2. sin(x) / cos(x)",
                "3. 1 / sin(x)",
                "4. cos(x) / sin(x)"
            ],
            "answer": "2"
        },
        {
            "question": "Which of the following is equal to sec²(x)?",
            "options": [
                "1. 1 + tan²(x)",
                "2. tan(x) + 1",
                "3. 1 + cot²(x)",
                "4. sin²(x) + tan²(x)"
            ],
            "answer": "1"
        }
    ]

    print("\nTrigonometric Identities Quiz")

    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        user_answer = input("Enter the number of your answer: ")

        if user_answer == q["answer"]:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer was option {q['answer']}.")


def inverse_trig_functions():
    """Quiz on inverse trig functions"""
    value = round(random.uniform(-1, 1), 2)

    print(f"\nWhat is arcsin({value}) in degrees?")
    input("Your answer: ")
    result = math.degrees(math.asin(value))
    print(f"The correct answer is: {round(result, 2)}°")


def trigonometric_equations():
    """Simple quiz on trig equations"""
    angle = random.choice([30, 45, 60])
    radians = math.radians(angle)
    value = round(math.sin(radians), 2)

    print(f"\nIf sin(x) = {value}, what is x in degrees between 0° and 90°?")
    input("Your answer: ")
    print(f"The correct answer is: {angle}°")


def trigonometric_functions():
    """Evaluate trig functions"""
    angle = random.randint(0, 90)
    radians = math.radians(angle)

    print(f"\nWhat is tan({angle}°)?")
    input("Your answer: ")

    if angle == 90:
        print("tan(90°) is undefined.")
    else:
        print(f"The correct answer is: {round(math.tan(radians), 2)}")

def trigonometry_menu():
    """Main menu for trigonometry topics."""
    print("\nWelcome to the Trigonometry Section!")

    while True:
        print("\nSelect a topic:")
        print("1. Unit Circle")
        print("2. Right Triangles")
        print("3. Trignometric Identities")
        print("4. Inverse Trigonometric Functions")
        print("5. Trigonometric Equations")
        print("6. Trigonometric Functions")
        print("7. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            print("You selected Unit Circle. Starting quiz...\n")
            unit_circle()
        elif choice == "2":
            print("Right Triangles. Starting quiz...\n")
        elif choice == "3":
            print("Trignometric Identities. Starting quiz...\n")
        elif choice == "4":
            print("Inverse Trigonometric Functions. Starting quiz...\n")
        elif choice == "5":
            print("Trigonometric Equations. Starting quiz...\n")
        else:
            print("Thank you for playing! Goodbye!")
            break
        


    
if __name__ == "__main__":
    trigonometry_menu()
