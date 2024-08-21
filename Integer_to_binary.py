def convert_to_8bit_binary():
    while True:
        # Prompting the user to input a number or quit
        user_input = input("Enter a non-negative integer to convert to 8 bits (or 'q' to quit): ")

        # Checking if the user wants to exit the program
        if user_input.lower() == 'q':
            print("Exiting the program. Goodbye!")
            break

        try:
            # Attempting to convert the input to an integer
            num = int(user_input)
            
            # Checking if the input number is non-negative
            if num < 0:
                print("Input must be a non-negative integer.")
            else:
                # Convert the number to an 8-bit binary string
                binary_representation = format(num, "08b")
                # Display the result
                print(f"Your number = {num} in binary = {binary_representation}")
        
        # Handling the case where the user input is not a valid integer
        except ValueError:
            print("Invalid input. Please enter a valid integer or 'q' to quit.")

# Calling the function to start the program
convert_to_8bit_binary()