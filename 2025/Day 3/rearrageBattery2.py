def maxJoltage(bank, k=12):
    maxVal = []
    removeNum = len(bank) - k
    
    for digit in bank:
        while maxVal and removeNum > 0 and maxVal[-1] < digit:
            maxVal.pop()
            removeNum -= 1
        maxVal.append(digit)

    return ''.join(maxVal[:k])

#dealing with the file
def fileProcess(filename):
    results = []
    with open(filename, 'r', encoding="utf-8") as file:
        
        #Read each line in the file
        for lineNum, line in enumerate(file, start=1):
            bank = line.strip()
            if not bank:
                continue
            solution = maxJoltage(bank)
            print(f"Line {lineNum}: {solution}")
            results.append(solution)
    return results

solution = fileProcess("input.txt")
result = 0

for num in solution:
    line = int(num)
    result += line
    print(f"Numbers added: {result}")

print(f"\nSolution: {result}")
