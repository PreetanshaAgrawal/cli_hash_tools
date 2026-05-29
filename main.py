import hashlib

def readFiles(names):
    """Read each input file and return a list of MD5 hashes with filenames."""
    ans = []
    for name in names:
        with open(name, "r", encoding="utf-8") as f:
            f_data = f.readlines()
        data = "".join(f_data)
        res = hashlib.md5(data.encode("utf-8")).hexdigest()
        res += f"#{name}"
        ans.append(res)
    return ans

def processText(data):
    """Compute the MD5 hash for a raw text string."""
    res = hashlib.md5(data.encode("utf-8")).hexdigest()
    res += f"#{data}"
    return [res]
    
def handleInputs(user_input):
    """Route the user input to file processing or raw text hashing."""
    if ".txt" in user_input:
        names = user_input.split(" ")
        ans = readFiles(names)
    else:
        ans = processText(user_input)
    return ans

# Create a registry map linking keywords to functions
COMMAND_MAP = {
    "md5sum": handleInputs,
}

def cliHandling(user_input):
    """Parse command input and dispatch the correct handler."""
    # Strip whitespace and split by the first space only
    parts = user_input.strip().split(maxsplit=1)
    
    if not parts:
        print("Error: Empty input.")
        return []

    keyword = parts[0].lower()  # Normalize keyword to lowercase
    
    # Capture everything else; default to empty string if no args provided
    remaining_input = parts[1] if len(parts) > 1 else ""

    if keyword in COMMAND_MAP:
        ans = COMMAND_MAP[keyword](remaining_input)
        return ans
    else:
        print(f"Error: Unknown keyword '{keyword}'. Available: {list(COMMAND_MAP.keys())}")
    return []

def formattingOutput(lst):
    """Print each result as <hash> <filename_or_text>."""
    for ele in lst:
        st = ele.split(
            "#"
        )
        print(f"{st[0]} {st[1]}")

if __name__ == "__main__":
    # Read a single line of input from the user and run the CLI processor
    filename = input("")
    ans = cliHandling(filename)
    formattingOutput(ans)