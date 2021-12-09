

def process_all_commands(command_lines, x, y):
    for line in command_lines:
        parts = line.split(' ')
        (x, y) = process_command(parts[0], parts[1], x, y)

    return x, y


def process_command(command, value, x, y):
    if command == 'down':
        y = y + int(value)
    elif command == 'up':
        y = y - int(value)
    elif command == 'forward':
        x = x + int(value)

    return x, y


inputFile = open("input")
output = process_all_commands(inputFile, 0, 0)
print(output)
print(output[0] * output[1])
