def safePassword(filename):

    #start position is 50
    position = 50
    zeroCount = 0

    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        print(f"Loaded {len(lines)} lines from {filename}")

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            direction = line[0]
            distance = int(line[1:])

            if direction == 'L':
                for _ in range(distance):
                    position = (position - 1) % 100
                    if position == 0:
                        zeroCount += 1
            elif direction == 'R':
                for _ in range(distance):
                    position = (position + 1) % 100
                    if position == 0:
                        zeroCount += 1
            else:
                raise ValueError(f"invalid rotation: {line}")
    return zeroCount

filename = "input.txt"
password = safePassword(filename)
print(password)