import hashlib

def readFiles(names):
    ans = []
    for name in names:
        with open(name, "r", encoding="utf-8") as f:
            f_data = f.readlines()
        data = "".join(f_data)
        res = hashlib.md5(data.encode("utf-8")).hexdigest()
        res += f"#{name}"
        ans.append(res)
    return ans

def handleMultipleFiles(filename):
    names = filename.split(" ")
    ans = readFiles(names)
    return ans

# 2. Create a registry map linking keywords to functions
COMMAND_MAP = {
    "md5sum": handleMultipleFiles,
}

def cliHandling(user_input):
    # Strip whitespace and split by the first space only
    parts = user_input.strip().split(maxsplit=1)
    
    if not parts:
        print("Error: Empty input.")
        return[]

    keyword = parts[0].lower() # Normalize keyword to lowercase
    
    # Capture everything else; default to empty string if no args provided
    remaining_input = parts[1] if len(parts) > 1 else ""

    # 3. Look up and execute the function
    if keyword in COMMAND_MAP:
        ans = COMMAND_MAP[keyword](remaining_input)
        return ans
    else:
        print(f"Error: Unknown keyword '{keyword}'. Available: {list(COMMAND_MAP.keys())}")
    return []

def formattingOutput(lst):
    pass

if __name__ == "__main__":
    filename = input("")
    print(f"User typed: {filename}")
    ans = cliHandling(filename)
    print("Success", ans)