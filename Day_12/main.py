def part1(lines):
    startingPoints = [l for l in lines if "start" in l]

    paths = []
    for point in startingPoints:
        p1, p2 = point.split('-')
        if p1 == 'start':
            paths.append([(p1, p2)])
        else:
            paths.append([(p2, p1)])

    newPaths = []
    for path in paths:
        currPoint = path[-1][1]
        possibleMoves = [tuple(m.split('-')) for m in lines if currPoint in m]
        for move in possibleMoves:
            if move in path:
                pass
        print(currPoint, possibleMoves)

    print(startingPoints)
    print(paths)


def part2(lines):
    pass


if __name__ == "__main__":

    with open('test_input.txt') as f:
        lines = [line.rstrip() for line in f.readlines()]

    print("\n----- Part 1 -----\n")
    part1(lines)
    print("\n----- Part 2 -----\n")
    part2(lines)
