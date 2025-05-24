# Author: Your Name
# Student ID: YourID
# Email ID: yourEmail
# This is my own work as defined by the University's Academic Misconduct Policy.

def print_student_info():
    print("Author: Your Name")
    print("Student ID: YourID")
    print("Email ID: yourEmail")
    print("This is my own work as defined by the University's Academic Misconduct Policy.\n")

def get_rule_binary(rule_number):
    # Return rule as an 8-bit binary string
    return format(rule_number, '08b')

def get_next_generation(current_gen, rule_bin):
    # Create the next generation based on the current one
    length = len(current_gen)
    next_gen = []
    for i in range(length):
        left = current_gen[(i - 1) % length]
        center = current_gen[i]
        right = current_gen[(i + 1) % length]
        pattern = f"{left}{center}{right}"
        index = int(pattern, 2)
        # Reverse index: 111=0, 000=7 (bit order in binary string)
        new_value = int(rule_bin[7 - index])
        next_gen.append(new_value)
    return next_gen

def display_generation(generation):
    # Convert 1 to 'X' and 0 to '.'
    print(''.join(['X' if cell == 1 else '.' for cell in generation]))

def get_initial_cells(input_type):
    if input_type == 'custom':
        raw_input = input("Enter custom binary string (e.g., 0100101): ")
        if not all(c in '01' for c in raw_input):
            raise ValueError("Custom input must only contain 0s and 1s.")
        return [int(c) for c in raw_input]
    elif input_type == 'standard':
        num_cells = int(input("Enter number of cells: "))
        if num_cells <= 0:
            raise ValueError("Number of cells must be positive.")
        cells = [0] * num_cells
        cells[num_cells // 2] = 1
        return cells
    else:
        raise ValueError("Invalid input type. Choose 'custom' or 'standard'.")

def main():
    try:
        print_student_info()

        rule_number = int(input("Enter rule number (0–255): "))
        if not 0 <= rule_number <= 255:
            raise ValueError("Rule number must be between 0 and 255.")

        generations = int(input("Enter number of generations: "))
        if generations < 0:
            raise ValueError("Generations must be a non-negative integer.")

        input_type = input("Enter input type (custom/standard): ").strip().lower()
        current_gen = get_initial_cells(input_type)

        rule_bin = get_rule_binary(rule_number)

        for _ in range(generations + 1):  # including initial
            display_generation(current_gen)
            current_gen = get_next_generation(current_gen, rule_bin)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
