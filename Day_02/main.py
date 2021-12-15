def part1():
    horizontal = 0
    depth = 0
    with open('input.txt') as f:
        for line in f:
            direction, changeVal = line.rstrip().split(' ')
            changeVal = int(changeVal)
            if direction == 'forward':
                horizontal += changeVal
            if direction == 'down':
                depth += changeVal
            if direction == 'up':
                depth -= changeVal

    print(
        f'Final horizontal: {horizontal}\n Final Depth: {depth}\n Total: {horizontal * depth}')


def part2():
    horizontal = 0
    depth = 0
    aim = 0
    with open('input.txt') as f:
        for line in f:
            direction, changeVal = line.rstrip().split(' ')
            changeVal = int(changeVal)
            if direction == 'forward':
                horizontal += changeVal
                depth += changeVal * aim
            if direction == 'down':
                aim += changeVal
            if direction == 'up':
                aim -= changeVal

    print(
        f'Final horizontal: {horizontal}\n Final Depth: {depth}\n Total: {horizontal * depth}')


if __name__ == "__main__":
    print("\n----- Part 1 -----\n")
    part1()
    print("\n----- Part 2 -----\n")
    part2()
