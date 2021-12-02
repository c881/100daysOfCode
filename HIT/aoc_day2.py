with open("day2_input.txt", "r") as i_file:
    lines = [line.split() for line in i_file.readlines()]
for i in range(len(lines)):
    lines[i] = (lines[i][0], int(lines[i][1]))
print(lines)

horizon = 0
depth = 0
aim = 0
for i in range(len(lines)):
    if lines[i][0] == 'forward':
        horizon += lines[i][1]
        depth += aim * lines[i][1]

    elif lines[i][0] == 'down':
        # depth += lines[i][1]
        aim += lines[i][1]
    elif lines[i][0] == 'up':
        # depth -= lines[i][1]
        aim -= lines[i][1]

print(f'{depth}, {horizon}, {depth*horizon}')