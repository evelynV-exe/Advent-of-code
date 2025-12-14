def isRepeated(s):
    length = len(s)
    for size in range(1, length // 2 + 1):
        if length % size == 0:
            if s == s[:size] * (length // size):
                return True
    return False

def checkingID(filename):

    ranges = []
    invalidIDs = []
    with open(filename, 'r', encoding='utf-8') as file:
        contents = file.read().strip()
        chunks = contents.split(",")

        for chunk in chunks:
            parts = chunk.split("-")
            if len(parts) == 2:
                start, end = map(int, parts)
                ranges.append((start, end))

                #check for invalid pattern
                for num in range(start, end + 1):
                    if isRepeated(str(num)):
                        invalidIDs.append(num)
            else: print(f"Invalid {chunk}")

    return ranges, invalidIDs

solution = 0
filename = "inputID.txt"
checkedID, invalidID = checkingID(filename)

print("Range: ")
for start, end in checkedID:
    print(f"Start: {start}, End: {end}")

print("Invalid IDs: ")
for invalid in invalidID:
    solution += invalid
    print(invalid)

print(f"Solution: {solution}")