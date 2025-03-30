degrees_to_coords = {

    "0 degree": (1, 0),
    "30 degrees": (math.sqrt(3)/2, 1/2),
    "45 degrees": (math.sqrt(2)/2, math.sqrt(2)/2),
    "60 degrees": (1/2, math.sqrt(3)/2),
    "90 degrees": (0, 1),
    "120 degrees": (-1/2, math.sqrt(3)/2),
    "135 degrees": (-math.sqrt(2)/2, math.sqrt(2)/2),
    "150 degrees": (-math.sqrt(3)/2, 1/2),
    "180 degrees": (-1, 0),
    "210 degrees": (-math.sqrt(3)/2, -1/2),
    "225 degrees": (-math.sqrt(2)/2, -math.sqrt(2)/2),
    "240 degrees": (-1/2, -math.sqrt(3)/2),
    "270 degrees": (0, -1),
    "300 degrees": (1/2, -math.sqrt(3)/2),
    "315 degrees": (math.sqrt(2)/2, -math.sqrt(2)/2),
    "330 degrees": (math.sqrt(3)/2, -1/2),
    "360 degrees": (1, 0)
}

value_to_angles = {
    ("sin", 1/2): ["30", "150"],
    ("sin", math.sqrt(2)/2): ["45", "135"],
    ("sin", math.sqrt(3)/2): ["60", "120"],
    ("sin", 1): ["90°"],

    ("cos", 1/2): ["60", "300"],
    ("cos", math.sqrt(2)/2): ["45", "315"],
    ("cos", math.sqrt(3)/2): ["30", "330"],
    ("cos", -0.5): ["120", "240"],
    ("cos", -1): ["180", "360"],
    
    ("tan", 1/3): ["30", "210"],
    ("tan", 1): ["45", "225"],
    ("tan", math.sqrt(3)): ["60", "240"],
    ("tan", 0): ["90", "270"],
    ("tan", -1/3): ["120", "300"],
    ("tan", -1): ["135", "315"],
    ("tan", -math.sqrt(3)): ["150", "330"],
    ("tan", "undefined"): ["180", "360"]
}


def normalize_angle(angle_str):
    """Converts '390 degrees' or '390' to normalized int like 30."""
    try:
        angle = int(angle_str.strip().replace('degrees', '').strip())
        return angle % 360
    except:
        return None

    

def corresponding_angles():
    """Part of unit_circle quiz. One of the random questions that can be asked."""
    key = random.choice(list(value_to_angles.keys()))
    trig_func, value = key
    angles = value_to_angles[key]
    if isinstance(value, str):  
        display_value = value
    else:
        display_value = Fraction(value).limit_denominator()

    print(f"\nWhat angle(s) in degrees correspond to {trig_func}(x) = {display_value}?")
    print("Example format: 30, 150, 390 (minimum 3 answers, can go beyond ±360°)")
    
    user_input = input("Your answers (comma separated): ")
    user_angles = [normalize_angle(a) for a in user_input.split(',')]
    user_angles = [a for a in user_angles if a is not None]

    if len(user_angles) < 3:
        print("Please enter at least three valid angles.\n")
        return

    
    correct_angles = [int(a) % 360 for a in angles]

    
    if all(ca in user_angles for ca in correct_angles):
        print("Correct!\n")
    else:
        print(f"Incorrect. Correct answers include: {', '.join(angles)}\n")

def unit_circle():
    """Quiz for unit circle."""
    print("\nWelcome to the Unit Circle Quiz!")

    question_types = [corresponding_angles, ]

    random.choice(question_types)()

   








def right_triangles():
    """questions for right triangles."""
    pass

def trigonometric_identities():
    """questions for trigonometric identities."""
    pass


def inverse_trigonometric_functions():
    """questions for inverse trigonometric functions."""
    pass

def trigonometric_equations():
    """questions for trigonometric equations."""
    pass

def trigonometric_functions():
    """questions for trigonometric functions."""
    pass
    
    