import sys

# 1. Define the functions that will handle the inputs
def handle_greet(args_string):
    print(f"Greeting logic executed with: '{args_string}'")

def handle_search(args_string):
    print(f"Searching database for: '{args_string}'")

# 2. Create a registry map linking keywords to functions
COMMAND_MAP = {
    "greet": handle_greet,
    "search": handle_search
}

def execute_command(user_input):
    # Strip whitespace and split by the first space only
    parts = user_input.strip().split(maxsplit=1)
    
    if not parts:
        print("Error: Empty input.")
        return

    keyword = parts[0].lower() # Normalize keyword to lowercase
    
    # Capture everything else; default to empty string if no args provided
    remaining_input = parts[1] if len(parts) > 1 else ""

    # 3. Look up and execute the function
    if keyword in COMMAND_MAP:
        COMMAND_MAP[keyword](remaining_input)
    else:
        print(f"Error: Unknown keyword '{keyword}'. Available: {list(COMMAND_MAP.keys())}")

# --- Example Usage ---
if __name__ == "__main__":
    # Simulate a user typing a full command line string
    test_input = input("")
    print(f"User typed: {test_input}")
    execute_command(test_input)

