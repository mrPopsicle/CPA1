import math
import random
from fractions import Fraction

def format_value(value):
    """
    Format mathematical values in a readable way.
    Handles special cases like square roots and fractions.
    """
    if isinstance(value, str):
        return value
    
    # Format square roots for readability
    if value == math.sqrt(2)/2:
        return "√2/2"
    elif value == math.sqrt(3)/2:
        return "√3/2"
    elif value == math.sqrt(3)/3:
        return "√3/3"
    elif value == math.sqrt(3):
        return "√3"
    elif value == -math.sqrt(2)/2:
        return "-√2/2"
    elif value == -math.sqrt(3)/2:
        return "-√3/2"
    elif value == -math.sqrt(3)/3:
        return "-√3/3"
    elif value == -math.sqrt(3):
        return "-√3"
    
    # For other values, use fractions for cleaner representation
    return str(Fraction(value).limit_denominator())


def unit_circle(question_type="random"):
    """
    Generate a question about basic trigonometric values (sin, cos, or tan).
    Returns a tuple: (question, correct_answer)
    """
    angles = [0, 30, 45, 60, 90, 120, 135, 150, 180, 
              210, 225, 240, 270, 300, 315, 330, 360]

    sin_values = {
         0:  0,
        30:  Fraction(1, 2),
        45:  Fraction(math.sqrt(2), 2),
        60:  Fraction(math.sqrt(3), 2),
        90:  1,
       120:  Fraction(math.sqrt(3), 2),
       135:  Fraction(math.sqrt(2), 2),
       150:  Fraction(1, 2),
       180:  0,
       210: -Fraction(1, 2),
       225: -Fraction(math.sqrt(2), 2),
       240: -Fraction(math.sqrt(3), 2),
       270: -1,
       300: -Fraction(math.sqrt(3), 2),
       315: -Fraction(math.sqrt(2), 2),
       330: -Fraction(1, 2),
       360:  0
    }

    cos_values = {
         0:  1,
        30:  Fraction(math.sqrt(3), 2),
        45:  Fraction(math.sqrt(2), 2),
        60:  Fraction(1, 2),
        90:  0,
       120: -Fraction(1, 2),
       135: -Fraction(math.sqrt(2), 2),
       150: -Fraction(math.sqrt(3), 2),
       180: -1,
       210: -Fraction(math.sqrt(3), 2),
       225: -Fraction(math.sqrt(2), 2),
       240: -Fraction(1, 2),
       270:  0,
       300:  Fraction(1, 2),
       315:  Fraction(math.sqrt(2), 2),
       330:  Fraction(math.sqrt(3), 2),
       360:  1
    }

    tan_values = {
         0:  0,
        30:  Fraction(math.sqrt(3), 3),
        45:  1,
        60:  math.sqrt(3),
       120: -math.sqrt(3),
       135: -1,
       150: -Fraction(math.sqrt(3), 3),
       180:  0,
       210:  Fraction(math.sqrt(3), 3),
       225:  1,
       240:  math.sqrt(3),
       300: -math.sqrt(3),
       315: -1,
       330: -Fraction(math.sqrt(3), 3),
       360:  0
    }

    # Angles where tan is undefined (90° and 270°)
    undefined_tan_angles = [90, 270]

    # Angles for which tan is defined
    tan_domain = []
    for angle in angles:
        if angle not in undefined_tan_angles:
            tan_domain.append(angle)


    if question_type == "random":
        question_type = random.choice(["sin", "cos", "tan"])

    angle = random.choice(tan_domain if question_type == "tan" else angles)

    if question_type == "sin":
        answer = sin_values[angle]
        question = f"Find the exact value of sin({angle}°)."

    elif question_type == "cos":
        answer = cos_values[angle]
        question = f"Find the exact value of cos({angle}°)."

    else:  # tan
        answer = tan_values[angle]
        question = f"Find the exact value of tan({angle}°)."

    return (question, answer)


def inverse_trig(question_type="random"):
    """
    Generate and solve inverse trigonometric function questions.

        

    """
    # Common values for inverse trig functions
    arcsin_values = {
        0: 0, 
        0.5: 30, 
        math.sqrt(2)/2: 45, 
        math.sqrt(3)/2: 60, 
        1: 90,
        -0.5: -30,
        -math.sqrt(2)/2: -45,
        -math.sqrt(3)/2: -60,
        -1: -90
    }
    
    arccos_values = {
        1: 0,
        math.sqrt(3)/2: 30,
        math.sqrt(2)/2: 45,
        0.5: 60,
        0: 90,
        -0.5: 120,
        -math.sqrt(2)/2: 135,
        -math.sqrt(3)/2: 150,
        -1: 180
    }
    
    arctan_values = {
        0: 0,
        math.sqrt(3)/3: 30,
        1: 45,
        math.sqrt(3): 60,
        -math.sqrt(3)/3: -30,
        -1: -45,
        -math.sqrt(3): -60
    }
    
    # Select question type if random
    if question_type == "random":
        question_type = random.choice(["arcsin", "arccos", "arctan"])
    
    # Choose value and generate question based on type
    if question_type == "arcsin":
        value = random.choice(list(arcsin_values.keys()))
        angle = arcsin_values[value]
        formatted_value = format_value(value)
        question = f"Find arcsin({formatted_value}) in degrees."
        answer = angle
      
        
    elif question_type == "arccos":
        value = random.choice(list(arccos_values.keys()))
        angle = arccos_values[value]
        formatted_value = format_value(value)
        question = f"Find arccos({formatted_value}) in degrees."
        answer = angle
        
        
    else:  # arctan
        value = random.choice(list(arctan_values.keys()))
        angle = arctan_values[value]
        formatted_value = format_value(value)
        question = f"Find arctan({formatted_value}) in degrees."
        answer = angle
        
    
    return (question, answer)

def right_triangle():
    """
    Generate and solve a right triangle problem.
    
    """
    # Standard angles for right triangles
    angle = random.choice([30, 45, 60])
    
    # Random side length with nice numbers
    hypotenuse = random.randint(5, 20)
    
    # Calculate other sides
    if angle == 30:
        opposite = hypotenuse / 2
        adjacent = hypotenuse * math.sqrt(3) / 2
    elif angle == 45:
        opposite = adjacent = hypotenuse / math.sqrt(2)
    else:  # angle == 60
        opposite = hypotenuse * math.sqrt(3) / 2
        adjacent = hypotenuse / 2
    
    # Round for cleaner problems
    hypotenuse = round(hypotenuse, 2)
    opposite = round(opposite, 2)
    adjacent = round(adjacent, 2)
    
    # Choose what to solve for
    problem_type = random.choice(["find_hypotenuse", "find_opposite", "find_adjacent", "find_angle"])
    
    if problem_type == "find_hypotenuse":
        question = f"In a right triangle, if one angle is {angle}° and the adjacent side to this angle is {adjacent}, find the hypotenuse."
        answer = hypotenuse
        
    elif problem_type == "find_opposite":
        question = f"In a right triangle, if one angle is {angle}° and the hypotenuse is {hypotenuse}, find the side opposite to this angle."
        answer = opposite
        
    elif problem_type == "find_adjacent":
        question = f"In a right triangle, if one angle is {angle}° and the side opposite to this angle is {opposite}, find the adjacent side."
        answer = adjacent
        
        
    else:  
        # Use a different angle to make the problem more interesting and dynamic also
        if angle == 30:
            other_angle = 60
        elif angle == 45:
            other_angle = 45
        else:  
            other_angle = 30
            
        question = f"In a right triangle, if the side opposite to an angle is {opposite} and the adjacent side is {adjacent}, find this angle in degrees."
        answer = other_angle
       
    return (question, answer)
