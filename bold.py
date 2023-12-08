def print_bold(text):
    # ANSI escape code for bold text
    bold_code = "\033[1m"
    
    # ANSI escape code to reset formatting
    reset_code = "\033[0m"

    # Print the text in bold
    print(f"{bold_code}{text}{reset_code}")

# Get input from the user
user_input = input("Enter text: ")

# Print the input in bold
print_bold(user_input)
