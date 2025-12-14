def safePassword(filename):

    #start position is 50
    position = 50
    zeroCount = 0

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            direction = line[0]
            distanceStr = line[1:]

            if not distanceStr.isdigit():
                raise ValueError(f"Invalid distance: {line}")
            distance = int(distanceStr)

            if direction == 'L':
                position = (position - distance) % 100
            elif direction == 'R':
                position = (position + distance) % 100
            else:
                raise ValueError(f"invalid rotation: {line}")
                        
            if position == 0:
                zeroCount += 1
    return zeroCount

filename = "input.txt"
password = safePassword(filename)
print(password)