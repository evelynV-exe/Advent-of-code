def maxJoltage(bank:str) -> int:
    maxVal = 0

    #choose the first digit
    for i in range(len(bank) - 1):

        #choose the second digit
        for j in range(i+1, len(bank)):

            #get the number
            joltage = int(bank[i] + bank[j])
            if joltage > maxVal:
                #set the max value to the highest nubmer that it found
                maxVal = joltage
    return maxVal

#dealing with the file
def fileProcess(filename):
    results = []
    with open(filename, 'r', encoding="utf-8") as file:
        
        #Read each line in the file
        for lineNum, line in enumerate(file, start=1):
            bank = line.strip()
            if not bank:
                continue
            print(f"line {lineNum}: {bank}")
            solution = maxJoltage(bank)
            print(f"Max joltage: {solution}")
            results.append(solution)
    return results

solution = fileProcess("input.txt")
result = 0

for num in solution:
    result += num
    print(f"Numbers added result: {result}")

print(f"\nSolution: {result}")