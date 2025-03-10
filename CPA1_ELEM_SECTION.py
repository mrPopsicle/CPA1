import random 

def generate_addition():
    """Generate an addition question."""

    a = int(random.randint(1, 100))
    b = int(random.randint(1, 100))
    print(a, "+", b)
    return a,b

def generate_subtraction():
    """Generate an subtraction question."""

    a = int(random.randint(1, 100))
    b = int(random.randint(1, 100))
    print(a, "-", b)
    return a,b   

def generate_multiplication():  
    """Generate an multiplication question."""
    
    a = int(random.randint(1, 100))
    b = int(random.randint(1, 100))
    print(a, "x", b)
    return a,b

def generate_division():  
    """Generate an division question."""
    
    a = b * int(random.randint(1, 100))
    b = int(random.randint(1, 100))
    print(a, "/", b)
    return a,b


def generate_pemdas():
    """Generate an pemdas question."""
    while True:

        a = int(random.randint(1, 20))
        b = int(random.randint(1, 20))
        c = int(random.randint(1, 20))
        d = int(random.randint(1, 20))

        operator1 =random.choice(["+", "-", "*", "//"])
        operator2 =random.choice(["+", "-", "*", "//"])
        operator3 =random.choice(["+", "-", "*", "//"])

        if operator1 == "//" and b != 0:
            a = b * random.randint(1, 10)
        if operator2 == "//" and c != 0:
            b = c * random.randint(1, 10)
        if operator3 == "//" and c != 0:
            c = d * random.randint(1, 10)


        expression = f"({a} {operator1} {b}) {operator2} ({c} {operator3} {d})"
        correct_answer = eval(expression)

        if isinstance(correct_answer, int):  # Ensure no decimal results
            return a, b, c, d, operator1, operator2, operator3

def exponentiation():
    """Generate an exponentiation question."""
    a = int(random.randint(1, 20))
    b = int(random.randint(1, 5))
    print(f"{a}^{b}")
    return a,b




        

def get_user_input():
    """Get the user's input for the question."""
    while True:
        try:
            user_input = int(input("Answer: "))
            return user_input
        except ValueError:
            print("Invalid input! Please enter a number.")

def math_practice_elem():
    """Main function to ask user for topic and generate a question."""
    print("\nWelcome to the Elementary Math Practice Program!")
    print("Select a topic:")
    
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. PEMDAS")
    print("6. Exponentiation")
    print("7. Exit")

    choice = input("Enter the number of the topic you would like to practice: ")

                    
    if choice == "1":
        a,b = generate_addition()
        print(f"What is the sum of {a} and {b}?")
        correct_answer = a + b
        user_answer = get_user_input()
        while user_answer != correct_answer:
            print(f"Incorrect. Try again\n")
            print(f"What is the sum of {a} and {b}?")
            user_answer = get_user_input()
        print("Correct!\n")
       

    elif choice == "2":
        a,b = generate_subtraction()
        print(f"What is the difference of {a} and {b}?") 
        user_answer = get_user_input()
        correct_answer = a - b
        while user_answer != correct_answer:
            print(f"Incorrect. Try again\n")
            print(f"What is the difference of {a} and {b}?") 
            user_answer = get_user_input()
        print("Correct!\n")

    elif choice == "3":
        a,b = generate_multiplication()
        print(f"What is the product of {a} and {b}? ")
        user_answer = get_user_input()
        correct_answer = a * b
        while user_answer != correct_answer:
            print(f"Incorrect. Try again\n")
            print(f"What is the product of {a} and {b}? ")
            user_answer = get_user_input()
        print("Correct!\n")

    elif choice == "4":
        a,b = generate_division()
        print(f"What is the quotient of {a} and {b}? ")
        user_answer = get_user_input()
        correct_answer = a / b
        while user_answer != correct_answer:
            print(f"Incorrect. Try again\n")
            print(f"What is the quotient of {a} and {b}? ")
            user_answer = get_user_input()
        print("Correct!\n")
    
    elif choice == "5":
        a,b,c,d,operator1,operator2,operator3 = generate_pemdas()
        print(f"What is the result of {a} {operator1} {b} {operator2} {c} {operator3} {d}? ")
        user_answer = get_user_input()
        correct_answer = eval(f"{a} {operator1} {b} {operator2} {c} {operator3} {d}")
        while user_answer != correct_answer:
            print(f"Incorrect. Try again\n")
            print(f"What is the result of {a} {operator1} {b} {operator2} {c} {operator3} {d}? ")
            user_answer = get_user_input()
        print("Correct!\n")
    
    elif choice == "6":
        a,b = exponentiation()
        print(f"What is the result of {a}^{b}? ")
        user_answer = get_user_input()
        correct_answer = a ** b
        while user_answer != correct_answer:
            print(f"Incorrect. Try again\n")
            print(f"What is the result of {a}^{b}? ")
            user_answer = get_user_input()
        print("Correct!\n")

    elif choice == "7":
        print("Goodbye!")
        exit()
    else:
        print("Invalid choice. Please try again.\n")

        

# if choice == "1":
#     sequence = generate_number_sequences()
#     print(f"What is the next number in this sequence: {sequence}") 
#     correct_answer = sequence[-1] + (sequence[1] - sequence[0])
#     while user_answer != correct_answer:
#         print(f"❌ Incorrect. Try again\n")
#         user_answer = get_user_input()
#     print("Correct!\n")


# def generate_number_sequences():
#     """Generate an arithmetic sequence question."""

#     start = random.randint(1, 20)
#     diff = random.randint(1,10)
#     length = random.randint(5, 10)

#     sequence = [start]

#     for i in range(length):

#         sequence.append(sequence[i-1] + diff)

#     return sequence

if __name__ == "__main__":
    math_practice_elem()