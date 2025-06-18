# Author: Saumya Patel
# Student ID: 110383897
# Email ID: patsy076@mymail.unisa.edu.au
# This is my own work as defined by the University's Academic Misconduct Policy.

def rule_to_binary(rule_number):
    # Convert rule number to 8-bit binary and reverse it
    # so index 0 corresponds to pattern 000 and index 7 to 111
    return format(rule_number, '08b')[::-1]

def next_generation(cells, rule_bin):
    # Generate the next generation of cells using the rule
    length = len(cells)
    new_gen = []
    for i in range(length):
        # Get the left, center, and right neighbors with wrap-around
        left = cells[(i - 1) % length]
        center = cells[i]
        right = cells[(i + 1) % length]

        # Form the neighborhood pattern as a 3-bit binary number
        pattern = int(f"{left}{center}{right}", 2)

        # Look up the next value using the rule binary
        new_value = int(rule_bin[pattern])
        new_gen.append(new_value)
    return new_gen

def display_generation(cells):
    # Print the generation: '.' for 0, 'X' for 1
    print(''.join('X' if c == 1 else '.' for c in cells))

def get_standard_input(num_cells):
    # Generate standard input: all 0s except center cell is 1
    cells = [0] * num_cells
    cells[num_cells // 2] = 1
    return cells

def get_custom_input():
    # Prompt user for custom binary string input
    raw = input("Enter custom binary string (e.g., 010101): ")
    if not all(c in '01' for c in raw):
        raise ValueError("Input must only contain 0s and 1s.")
    return [int(c) for c in raw]

def main():
    # Print user details and declaration
    print("Author: Saumya Patel")
    print("Student ID: 110383897")
    print("Email ID: patsy076@mymail.unisa.edu.au")
    print("This is my own work as defined by the University's Academic Misconduct Policy.\n")

    try:
        # Get the rule number from user
        rule_number = int(input("Enter rule number (0-255): "))
        if rule_number < 0 or rule_number > 255:
            raise ValueError("Rule number must be between 0 and 255.")

        # Get the number of generations to simulate
        generations = int(input("Enter number of generations: "))
        if generations < 0:
            raise ValueError("Number of generations must be non-negative.")

        # Ask user to choose between standard or custom input
        input_type = input("Input type (standard/custom): ").strip().lower()

        # Initialize the input cell configuration
        if input_type == 'standard':
            num_cells = int(input("Enter number of cells: "))
            cells = get_standard_input(num_cells)
        elif input_type == 'custom':
            cells = get_custom_input()
        else:
            raise ValueError("Invalid input type. Use 'standard' or 'custom'.")

        # Convert rule number to binary pattern string
        rule_bin = rule_to_binary(rule_number)

        # Display each generation
        for _ in range(generations + 1):  # include initial generation
            display_generation(cells)
            cells = next_generation(cells, rule_bin)

    except Exception as e:
        # Catch and print any errors that occur during input or processing
        print(f"Error: {e}")

if __name__ == '__main__':
    main()

