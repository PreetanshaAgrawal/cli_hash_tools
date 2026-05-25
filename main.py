import hashlib

def readFiles(names):
    ans = []
    for name in names:
        with open(name, "r", encoding="utf-8") as f:
            f_data = f.readlines()
        data = "".join(f_data)
        # Add name of file with res
        res = hashlib.md5(data.encode("utf-8")).hexdigest()
        ans.append(res)
    return ans

def handleMultipleFiles(filename):
    names = filename.split(" ")
    ans = readFiles(names)
    return ans

if __name__ == "__main__":
    filename = input("Enter the name of the file : ")
    res = handleMultipleFiles(filename)
    print(f"MD5 : {res}")