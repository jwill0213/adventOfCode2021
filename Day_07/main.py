def part1():
    with open('input.txt') as f:
        lines = [line.rstrip() for line in f.readlines()]

    crabList = [int(f) for f in lines[0].split(',')]
    crabList.sort()

    # Loop to the max value
    minimumFuel = None
    for pos in range(crabList[-1]+1):
        fuelUsed = sum([abs(pos-x) for x in crabList])
        if minimumFuel is None or fuelUsed < minimumFuel:
            minimumFuel = fuelUsed

    print(f"Minimum Fuel: {minimumFuel}")


def part2():
    with open('input.txt') as f:
        lines = [line.rstrip() for line in f.readlines()]

    crabList = [int(f) for f in lines[0].split(',')]
    crabList.sort()

    # Loop to the max value
    minimumFuel = None
    for pos in range(crabList[-1]+1):
        sumList = [(f'{x} -> {pos}', abs(pos-x), sum(range(1, abs(pos-x)+1)))
                   for x in crabList]
        fuelUsed = sum([s[2] for s in sumList])
        if minimumFuel is None or fuelUsed < minimumFuel:
            minimumFuel = fuelUsed

    print(f"Minimum Fuel: {minimumFuel}")


if __name__ == "__main__":
    print("\n----- Part 1 -----\n")
    part1()
    print("\n----- Part 2 -----\n")
    part2()
